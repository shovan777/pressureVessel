import React, {Component} from 'react';
import Aux from '../../hoc/Aux/Aux';
import Modal from '../../components/UI/Modal/Modal';
import Button from '../../components/UI/Button/Button';
import Parameter from '../../components/Parameter';
import Parameter1 from '../../components/UI/Parameter/Parameter1/Parameter1';
import Parameter2 from '../../components/UI/Parameter/Parameter2/Paramater2';
import ThreeScene from '../../components/ThreeComponents/ThreeScene/ThreeScene';
import Toolbar from '../../components/Navigation/Toolbar/Toolbar';
import NavBar from '../../components/Navigation/NavigationItems/NavBar';
class VesselBuilder extends Component {
    state = {
        showParam : false,
        showParam1: true,
        params1: {
            material: "",
            ip: 0,
            temp1:0,
            ep: 0,
            temp2:0,
            ih: false,
            ci: 0,
            co: 0
            
        },
        params2: {
            hd: 0,
            mht: 0,
            sfl: 0,
            nsrt: 0,
            hr: 0,
        }
    }

    showBuildParams = () => {
        this.setState({showParam: true});
    }

    submitParamsHandler1 = (event) => {
        //this.setState({showParam: false});
        this.setState({showParam1: false});
        this.setState({params1:event});
        console.log(event)
    }

    submitParamsHandler2 = (event) => {
        this.setState({showParam: false});
        this.setState({showParam1: true});
        this.setState({params2:event});
        console.log(event)
    }

    cancelParamsHandler = () => {
        this.setState({showParam: false});
    }

    previousParamsHandler = () => {
        this.setState({showParam1: true});
    }
    
    render() {

        console.log("Rerendered");
        return(
            <Aux>
                <Modal show={this.state.showParam}>
                    <Parameter1
                        show = {this.state.showParam1} 
                        submitParams = {this.submitParamsHandler1}
                        cancelParams = {this.cancelParamsHandler}
                        />
                    <Parameter2 
                        show = {!this.state.showParam1} 
                        submitParams = {this.submitParamsHandler2}
                        cancelParams = {this.cancelParamsHandler}
                        previousParams = {this.previousParamsHandler}
                        min1 = {0.3625}
                        min2 = {0.3625}
                        />
                </Modal>
                <Toolbar />
                <ThreeScene length={this.state.params1.ip}/>
                <Button btnType="Success" clicked={this.showBuildParams}>BUILD</Button>

            </Aux>
        );
    }
}

export default VesselBuilder;
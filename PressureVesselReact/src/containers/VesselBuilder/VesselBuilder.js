import React, {Component} from 'react';
import Aux from '../../hoc/Aux/Aux';
import Modal from '../../components/UI/Modal/Modal';
import Modal1 from '../../components/UI/Modal/Modal1';

import Button from '../../components/UI/Button/Button';
import Parameter from '../../components/Parameter';
import Parameter1 from '../../components/UI/Parameter/Parameter1/Parameter1';
import Parameter2 from '../../components/UI/Parameter/Parameter2/Parameter2';
import Parameter3 from '../../components/UI/Parameter/Parameter3/Parameter3';
import ThreeScene from '../../components/ThreeComponents/ThreeScene/ThreeScene';
import Toolbar from '../../components/Navigation/Toolbar/Toolbar';
import axios from '../../axios';
import Data from '../../components/UI/Data/Data';
class VesselBuilder extends Component {
    state = {
        showParam : false,
        showParam1: true,
        showParam3: true,
        showCylinder: false,
        showEllipsoid: false,
        cylinder: false,
        ellipsoid: false,
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
        },
        params3: {
            material: "",
            ip: 0,
            temp1:0,
            ep: 0,
            temp2:0,
            ih: false,
            ci: 0,
            co: 0
        },
        params4: {
            sd: 0,
            l: 0,
            t: 0
        },
        params5: {
            mawp: 200,
            map: 241.44,
            maep: 55.67,
            sfi: 0.365,
            sfo: 0.1404,
            mdmt: 23.2,
            sfmawp: 206.61,
            sfmap:248.14,
            sfmaep: 188.22
        }
    }

    // showBuildParams = () => {
    //     this.setState({showParam: true});
    // }

    submitParamsHandler1 = (event) => {
        //this.setState({showParam: false});
        
        if(this.state.showCylinder) {
            this.setState({params3:event});
            this.setState({showParam3: false});
        } else if(this.state.showEllipsoid) {
            this.setState({params1 :event});
            this.setState({showParam1: false});
        }
        // console.log(event)
    }

    submitParamsHandler2 = (event) => {
        this.setState({showParam: false});
        this.setState({showParam1: true});
        this.setState({params2:event});
        this.setState({ellipsoid: true});
        // console.log(event)
    }

    submitParamsHandler3 = (event) => {
        this.setState({showParam: false});
        this.setState({showParam3: true});
        this.setState({params4:event});
        this.setState({cylinder: true});
        console.log(this.state);
    }

    cancelParamsHandler = () => {
        this.setState({showParam: false,showCylinder:false, showCylinder:false,
        showParam1: true, showParam3:true});
    }

    previousParamsHandler = () => {
        if(this.state.showEllipsoid) {
        this.setState({showParam1: true});
        } else if(this.state.showCylinder) {
            this.setState({showParam3: true});
        }
    }

    resetThenSet= (id) => {
        this.setState({showParam: true});
        if(id === 0) {
            this.setState({showParam: true,showCylinder: true,
            showEllipsoid: false});
        } else if(id === 1) {
            this.setState({showParam: true,showCylinder: false,
                showEllipsoid: true});
        }
        
    }

    getRequest = () => {
        axios.get("/polls/" + 5)
          .then(response => {
            console.log(response);
          })
          .catch(error => {
              this.setState({error: true});
              //console.log(error);
          });
    }

    postRequest = () => {
        axios.post("/polls/",this.state)
            .then(response => {
                console.log(response);
            });
    }
    
    render() {

        // console.log("Rerendered");
        return(
            <Aux>
                <Modal show={this.state.showParam && this.state.showEllipsoid}>
                    <Parameter1
                        label = {"Ellipsoidal Head"}
                        show = {this.state.showParam1} 
                        submitParams = {this.submitParamsHandler1}
                        cancelParams = {this.cancelParamsHandler}
                        />
                    <Parameter2 
                        label = {"Ellipsoidal Head Dimensions"}
                        show = {!this.state.showParam1} 
                        submitParams = {this.submitParamsHandler2}
                        cancelParams = {this.cancelParamsHandler}
                        previousParams = {this.previousParamsHandler}
                        min1 = {0.3625}
                        min2 = {0.3625}
                        />
                </Modal>
                <Modal1 show={this.state.showParam && this.state.showEllipsoid && !this.state.showParam1}>
                <Data
                        map={this.state.params5.map}
                        maep={this.state.params5.maep}
                        mawp={this.state.params5.mawp}
                        sfi={this.state.params5.sfi}
                        sfo={this.state.params5.sfo}
                        sfmap={this.state.params5.sfmap}
                        sfmawp={this.state.params5.sfmaep}
                        sfmaep={this.state.params5.sfmawp}
                        mdmt={this.state.params5.mdmt}/>
                </Modal1>
                <Modal show={this.state.showParam && this.state.showCylinder}>
                    <Parameter1
                        label = {"Cylinder"}
                        show = {this.state.showParam3} 
                        submitParams = {this.submitParamsHandler1}
                        cancelParams = {this.cancelParamsHandler}
                        />
                    <Parameter3 
                        label = {"Cylinder Dimensions"}
                        show = {!this.state.showParam3} 
                        submitParams = {this.submitParamsHandler3}
                        cancelParams = {this.cancelParamsHandler}
                        previousParams = {this.previousParamsHandler}
                        min = {0.3625}
                        />
                </Modal>
                <Modal1 show={this.state.showParam && this.state.showCylinder && !this.state.showParam3}>
                    <Data
                        map={this.state.params5.map}
                        maep={this.state.params5.maep}
                        mawp={this.state.params5.mawp}
                        sfi={this.state.params5.sfi}
                        sfo={this.state.params5.sfo}
                        sfmap={this.state.params5.sfmap}
                        sfmawp={this.state.params5.sfmaep}
                        sfmaep={this.state.params5.sfmawp}
                        mdmt={this.state.params5.mdmt}/>
                </Modal1>
                <Toolbar 
                resetThenSet={this.resetThenSet}/>
                <ThreeScene showC={this.state.cylinder} showE={this.state.ellipsoid}/>
                {/* <Button btnType="Success" clicked={this.showBuildParams}>BUILD</Button> */}

            </Aux>
        );
    }
}

export default VesselBuilder;
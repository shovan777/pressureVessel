import React,{Component} from 'react';
import Aux from '../hoc/Aux/Aux';
import Input from './UI/Input/Input';
import Button from '../components/UI/Button/Button';
import classes from './Parameter.css';
const inputVar = [
    {label:'Material', type:'dropdown', id:1},
    {label:'Internal Pressure', type:'number', id:2},
    {label:'External Pressure', type:'number', id:3},
    {label:'Height', type:'number', id:4},
    {label:'Internal Head', type:'checkbox', id:5},
    {label:'Corrosion Inner', type:'number', id:6},
    {label:'Corrosion Outer', type:'number', id:7}
]

class Parameter extends Component {

    state = {
        params: {
            m: 0,
            ip: 0,
            ep: 0,
            h: 0,
            ih: false,
            ci: 0,
            co: 0
        },
        showNext: false
    }
    inputChangeHandler = (event) => {
        const updatedParams = {
            ...this.state.params
        };
        updatedParams[event.target.name] = event.target.value;
        this.setState({params:updatedParams});
    }

    render() {
        return(
            <Aux>
            <form>  
            {inputVar.map(invar => (
                <div key={invar.id} className={classes.Input}>
                    <label className={classes.Label}>{invar.label}</label>
                    <input name={invar.id} type={invar.type} placeholder="0" className={classes.InputElement}
                        onChange= {this.inputChangeHandler} />
                 </div>
            ))
            }
            </form>
            <Button btnType="Success" clicked={() => this.props.submitParams(this.state.params)}>NEXT</Button>
            <Button btnType="Danger" clicked={this.props.cancelParams}>CANCEL</Button>
            </Aux>
        );
    }
}

export default Parameter;
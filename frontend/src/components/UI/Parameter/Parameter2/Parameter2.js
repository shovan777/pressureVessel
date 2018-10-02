import React, { Component } from 'react';
import Aux from '../../../../hoc/Aux/Aux';
import Button from '../../Button/Button';
import classes from './Parameter2.css';
const inputVar = [
    { label: 'Material', type: 'dropdown', id: 1 },
    { label: 'Internal Pressure', type: 'number', id: 2 },
    { label: 'External Pressure', type: 'number', id: 3 },
    { label: 'Height', type: 'number', id: 4 },
    { label: 'Internal Head', type: 'checkbox', id: 5 },
    { label: 'Corrosion Inner', type: 'number', id: 6 },
    { label: 'Corrosion Outer', type: 'number', id: 7 }
]

class Parameter1 extends Component {

    state = {
        params: {
            hd: 0,
            mht: 0,
            sfl: 0,
            nsrt: 0,
            hr: 0,
        },
        showNext: false
    }
    materialHandler = (event) => {
        const updatedParams = {
            ...this.state.params
        };
        updatedParams[event.target.name] = event.target.value;
        this.setState({ params: updatedParams });
    }

    render() {

        let form = null;
        if (this.props.show) {
            form = (
                <div>
                    <div className={classes.Input}>
                    <label className={classes.Label2}>{this.props.label}</label>
                    </div>
                    <form>
                        
                        <div className={classes.Input}>
                            <label className={classes.Label}>Head Diameter</label>
                            <input name="hd" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.materialHandler} />
                        </div>
                        <div className={classes.Input}>
                            <label className={classes.Label}>Minimum Head Thickness</label>
                            <input name="mht" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.materialHandler} />
                            <label className={classes.Label1}>{this.props.min1} min</label>
                        </div>

                        <div className={classes.Input}>
                            <label className={classes.Label}>Straight Range Length</label>
                            <input name="sfl" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.materialHandler} />
                        </div>
                        <div className={classes.Input}>
                            <label className={classes.Label}>Nominal Str Range Thickness</label>
                            <input name="nsrt" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.materialHandler} />
                            <label className={classes.Label1}>{this.props.min2} min</label>
                        </div>

                        <div className={classes.Input}>
                            <label className={classes.Label}>Head Ratio</label>
                            <input name="hr" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.materialHandler} />
                        </div>

                    </form>
                    <Button btnType="Success" clicked={this.props.previousParams}>Previous</Button>
                    <Button btnType="Success" clicked={() => this.props.submitParams(this.state.params)}>Submit</Button>
                    <Button btnType="Danger" clicked={this.props.cancelParams}>Cancel</Button>
                    
                </div>
            );
        } else {
            form = null;
        }
        return (
            <Aux>
                {form}

            </Aux>
        );
    }
}

export default Parameter1;
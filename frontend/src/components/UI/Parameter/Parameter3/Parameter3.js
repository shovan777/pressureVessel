import React, { Component } from 'react';
import Aux from '../../../../hoc/Aux/Aux';
import Button from '../../Button/Button';
import classes from './Parameter3.css';
const inputVar = [
    { label: 'Shell Diameter', type: 'number', id: 1 },
    { label: 'Length', type: 'number', id: 2 },
    { label: 'Thickness', type: 'number', id: 3 }

]

class Parameter3 extends Component {

    state = {
        params: {
            sd: 0,
            l: 0,
            t: 0
        },
        showNext: false
    }
    inputHandler = (event) => {
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
                            <label className={classes.Label}>Shell Diameter</label>
                            <input name="sd" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.inputHandler} />
                        </div>
                        <div className={classes.Input}>
                            <label className={classes.Label}>Length</label>
                            <input name="l" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.inputHandler} />
                        </div>

                        <div className={classes.Input}>
                            <label className={classes.Label}>Thickness</label>
                            <input name="t" type="number" placeholder="0.0" className={classes.InputElement}
                                onChange={this.inputHandler} />
                            <label className={classes.Label1}>{this.props.min} min</label>
                        </div>

                    </form>
                    <Button btnType="Success" clicked={this.props.previousParams}>Previous</Button>
                    <Button btnType="Success" clicked={() => this.props.submitParams(this.state.params)}>Submit</Button>
                    <Button btnType="Success" disabled={this.props.btndisabled} clicked={this.props.finish2}>Finish</Button>
                    <Button btnType="Danger" disabled={!this.props.btndisabled} clicked={this.props.cancelParams}>Cancel</Button>

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

export default Parameter3;

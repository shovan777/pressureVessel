import React,{Component} from 'react';
import classes from './Modal1.css';
import Aux from '../../../hoc/Aux/Aux';
class Modal extends Component {

    render () {
        return (
        <Aux>
            <div 
                className = {classes.Modal}
                style={{
                    transform: this.props.show ? 'translateY(0)' : 'translateY(-100vh)',
                    opacity: this.props.show? '1':'0'

                }}>
                {this.props.children}
            </div>
        </Aux>
        );
    }
}

export default Modal;
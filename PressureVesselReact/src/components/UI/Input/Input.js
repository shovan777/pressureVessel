import React from 'react';
import classes from './Input.css';
const input = (props) => {

    return (
        <div className={classes.Input}>
            <label className={classes.Label}>{props.label}</label>
            <input type="number" placeholder="0.0" className={classes.InputElement}
                value={props.value}
                onChange= {props.changed}
                {...props} />
        </div>

    );
}

export default input;
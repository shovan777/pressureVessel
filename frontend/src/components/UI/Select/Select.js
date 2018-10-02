import React from 'react';

const Select = (props) => {

    
    const opts = props.options;
    console.log(opts);
    return(
    <div>
        <select 
        {...opts.map(option => (
            <option key={option.value} value={option.value}>{option.label}</option>
            ))
            }
            onChange={props.onchange}>

        </select>
        </div>
    );
}

export default Select;
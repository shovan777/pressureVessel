import React,{Component} from 'react';
import classes from './NavigationItems.css';
import NavigationItem from './NavigationItem/NavigationItem';
import Dropdown from '../DropDown/Dropdown';
class NavigationItems extends Component {

   
    render() {
        return(
    <ul className={classes.NavigationItems}>
        <NavigationItem >File</NavigationItem>
        <NavigationItem>Component</NavigationItem>
        <NavigationItem>Nozzle</NavigationItem>
    </ul>
        );
    }
}

export default NavigationItems;
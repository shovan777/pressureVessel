import React from 'react';
import classes from './NavigationItems.css';
import NavigationItem from './NavigationItem/NavigationItem';

const navigationItems =() => (
    <ul className={classes.NavigationItems}>
        <NavigationItem >File</NavigationItem>
        <NavigationItem>Component</NavigationItem>
        <NavigationItem >Action</NavigationItem>
        <NavigationItem>Nozzle</NavigationItem>
        <NavigationItem >Attach</NavigationItem>
        <NavigationItem>Support</NavigationItem>
        <NavigationItem >Codes</NavigationItem>
        <NavigationItem>Loads</NavigationItem>
        <NavigationItem >Materials</NavigationItem>
        <NavigationItem >Forms</NavigationItem>
        <NavigationItem >Window</NavigationItem>
        <NavigationItem >Help</NavigationItem>
    </ul>
);

export default navigationItems;
import React, { Component } from 'react';
import classes from './Toolbar.css';
import cls from '../NavigationItems/NavigationItems.css';
import NavigationItem from '../NavigationItems/NavigationItem/NavigationItem';
import Dropdown from '../DropDown/Dropdown';
class Toolbar extends Component {


    state = {
        geometry: [
            {
                id: 0,
                title: 'Cylinder',
                selected: false,
                key: 'geometry'
            },
            {
                id: 1,
                title: 'Ellipsoidal Head',
                selected: false,
                key: 'geometry'
            }
        ]
    }

    toggleSelected = (id, key) => {
        let temp = [...this.state[key]]
        temp[id].selected = !temp[id].selected
        this.setState({
            [key]: temp
        })
    }

    resetThenSet = (id, stateKey) => {
        let geometry = [...this.state.geometry]
        geometry.forEach(item => item.selected = false);
        geometry[id].selected = true;
        this.setState({ geometry: geometry },
            this.props.resetThenSet(id))
        // console.log(id);
    }
    render() {
        return (
            <header className={classes.Toolbar}>
                {/* <NavigationItems/> */}
                <ul className={cls.NavigationItems}>
                    <NavigationItem >File</NavigationItem>
                    <NavigationItem>Component</NavigationItem>
                    <NavigationItem>Nozzle</NavigationItem>

                    <div className="wrapper">
                        <Dropdown
                            title="Action"
                            list={this.state.geometry}
                            resetThenSet={this.resetThenSet}
                        />
                    </div>
                </ul>
            </header>
        );
    }
}

export default Toolbar;
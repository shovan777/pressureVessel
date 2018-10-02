import React from 'react';
import classes from './Data.css';
const Data = (props) => (

    <div className={classes.Data}>
    <p>MAWP = {props.mawp} psi</p>
    <p>MAP = {props.map} psi</p>
    <p>MAEP = {props.maep} psi</p>
    <p>SF t(int) = {props.sfi} "</p>
    <p>SF t(ext) = {props.sfo} "</p>
    <p>SF Rated MDMT= {props.mdmt} deg F</p>
    <p>SF MAWP= {props.sfmawp} psi</p>
    <p>SF MAP= {props.sfmap} psi</p>
    <p>SF MAEP= {props.sfmaep} psi</p>

    
    </div>
);

export default Data;
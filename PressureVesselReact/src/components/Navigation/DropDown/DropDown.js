import React,{Component} from 'react';
import classes from './DropDown.css';

class Dropdown extends Component {
    constructor(){
     super();
    
     this.state = {
           displayMenu: false,
         };
    
      this.showDropdownMenu = this.showDropdownMenu.bind(this);
      this.hideDropdownMenu = this.hideDropdownMenu.bind(this);
    
    };
    
    showDropdownMenu = (event) => {
        console.log("Button clicked");
        this.setState({displayMenu: true});
        // event.preventDefault();
        // this.setState({ displayMenu: true }, () => {
        // document.addEventListener('click', this.hideDropdownMenu);
        // });
      }
    
      hideDropdownMenu = () => {
        this.setState({ displayMenu: false }, () => {
          document.removeEventListener('click', this.hideDropdownMenu);
        });
    
      }
    
      render() {

        let dropdownshow = null;
        if(this.state.displayMenu) {
            dropdownshow = (
                <ul>
             <li><a className={classes.active} href="#Create Page">Create Page</a></li>
             <li><a href="#Manage Pages">Manage Pages</a></li>
             <li><a href="#Create Ads">Create Ads</a></li>
             <li><a href="#Manage Ads">Manage Ads</a></li>
             <li><a href="#Activity Logs">Activity Logs</a></li>
             <li><a href="#Setting">Setting</a></li>
             <li><a href="#Log Out">Log Out</a></li>
            </ul>
            )
        } else {
            dropdownshow = null;
        }
        return (
            <div  className={classes.dropdown} style = {{background:"#703B09",width:"200px"}} >
             <div className={classes.button} onClick={this.showDropdownMenu}> My Setting </div>
    
              {dropdownshow}
    
           </div>
    
        );
      }
    }
    
    export default Dropdown;
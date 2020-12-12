import React from "react";
import {Link} from "react-router-dom";
import "./SignUp.scss";

const SignUp = () =>{
    return(
       <div className={"sign-up"}>
           <h4>Sign Up</h4>
           <div className="row">
               <form className="col s12">
                   <div className="row">
                       <div className="input-field col s5">
                           <input id="first_name" type="text" className="validate"/>
                               <label htmlFor="first_name">First Name</label>
                       </div>
                       <div className="input-field col s5">
                           <input id="last_name" type="text" className="validate"/>
                               <label htmlFor="last_name">Last Name</label>
                       </div>
                   </div>
                   <div className="row">
                       <div className="input-field col s10">
                           <input id="email" type="email" className="validate"/>
                           <label htmlFor="email">Email</label>
                       </div>
                   </div>
                   <div className="row">
                       <div className="input-field col s10">
                           <input id="password" type="password" className="validate"/>
                               <label htmlFor="password">Password</label>
                       </div>
                   </div>
                   <div className="row">
                       <div className="input-field col s10">
                           <input id="password" type="password" className="validate"/>
                           <label htmlFor="password">Confirm Password</label>
                       </div>
                   </div>
               </form>
           </div>
           <a className="waves-effect waves-teal btn-flat">Sign Up</a>
           <p>Already have a account , <Link to={"/login"}>Log In</Link></p>
       </div>
    )
};

export default SignUp;

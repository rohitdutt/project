import React from "react";
import "./LogIn.scss";
import {Link} from "react-router-dom";

const LogIn = () =>{
    return(
        <div className={"log-in"}>
            <h3>Log In</h3>
            <div className="row">
                <form className="col s10">
                    <div className="row">
                        <div className="input-field col s12">
                            <input id="email" type="email" className="validate"/>
                            <label htmlFor="email">Email</label>
                        </div>
                    </div>
                    <div className="row">
                        <div className="input-field col s12">
                            <input id="password" type="password" className="validate"/>
                                <label htmlFor="password">Password</label>
                        </div>
                    </div>
                </form>
            </div>
            <a className="waves-effect waves-teal btn-flat">Log In</a>
            <p>Want to Sign Up with us , <Link to={"/signup"}>Sign Up</Link></p>
        </div>
    )
};

export default LogIn;

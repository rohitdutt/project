import React from "react";
import "./Navbar.scss";
import {Link} from "react-router-dom";

const Navbar = () =>{
    return(
        <div className={"nav-bar"}>
            <nav>
                <h3>Chit Chat</h3>
                <div className={"nav-bar-user-button"}>
                    <Link to={"/signup"}>
                        <a id={"sign-up"} className="waves-effect waves-teal btn-flat">Sign Up</a>
                    </Link>
                    <Link to={"/login"}>
                        <a className="waves-effect waves-teal btn-flat">Log In</a>
                    </Link>
                </div>
            </nav>
        </div>
    )
};

export default Navbar;

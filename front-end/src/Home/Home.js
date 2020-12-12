import React , {useState}from "react";
import Navbar from "../Navbar/Navbar";
import ChatBox from "../ChatBox/ChatBox";

const Home = () =>{
    const [user , setUser] = useState("rohitdutt");

    return(
        <div>
           <Navbar/>
           <ChatBox user={user}/>
        </div>
    )
};

export default Home;

import React , {useState , useEffect} from "react";
import Socket from "socket.io-client";
import "./ChatBox.scss";

const ChatBox = ({user}) => {
    let socket;

    const [port , setPort] = useState("http://localhost:4000/")
    const [messageToSend,setMessageToSend] = useState("");

    useEffect(()=>{
        socket = Socket(port);
        socket.on('typing', user =>{
            console.log(user);
          document.getElementById('typing').innerHTML = '<p><em>' + user + ' is typing a message...</em></p>';
        });

        socket.on('chat', messageToSend =>{
        document.getElementById('typing').innerHTML = '';
        document.getElementById('message').innerHTML += '<p><strong>' + user + ': </strong>' + messageToSend + '</p>';
        });
    },[])

    return(
        <div className={"chatbox"}>
            <h4>Server name</h4>
            <div className={"chat"}>
                <div id={"typing"} className={"is-typing"}/>
                <div id={"message"} className={"messages"}/>
            </div>
                <div className="row">
                    <form className="col s12">
                        <div className="row">
                            <div className="input-field col s12">
                                <textarea id="textarea1" className="materialize-textarea" onChange={(e)=>{
                                        setMessageToSend(e.target.value);
                                        console.log(messageToSend);
                                        // socket.emit('typing', user);
                                }}/>
                                <label htmlFor="textarea1">Message</label>
                            </div>
                        </div>
                    </form>
                    <button id={"send"} className="btn waves-effect waves-light" type="submit" name="action" onClick={()=>{
                        socket.emit('chat' , messageToSend);
                        console.log(messageToSend);
                        setMessageToSend("");
                        document.getElementById('textarea1').value = "";
                    }}>Send
                        <i className="material-icons right">send</i>
                    </button>
                </div>
        </div>
    )
};

export default ChatBox;

import './App.css';
import {Route ,Switch} from "react-router-dom";
import LogIn from "./User/LogIn";
import Home from "./Home/Home";
import SignUp from "./User/SignUp";

function App() {
  return (
    <div className="App">
        <Switch>
            <Route exact path={"/"} component={Home}/>
            <Route exact path = "/login" component = {LogIn} />
            <Route exact path = "/signUp" component = {SignUp} />
        </Switch>
    </div>
  );
}

export default App;

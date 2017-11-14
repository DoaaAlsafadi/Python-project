import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';

class App extends Component {

constructor(props){
  super(props);
  this.state = {
    userName:'',
    password:''
  }
}
sendData(){
 fetch('http://127.0.0.1:5000/login', {
        method: 'POST',
        headers: {
          Accept: 'application/json',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          userName:this.state.userName,
          password:this.state.password
        })
      })
        .then(response => {
          return response.json();
        })
        .then(responseJson => {
          console.log("Successssssssss !!!")
        })
        .catch(error => {
           console.log("Eroooooooooooooooooor !!!")
        });
    } 

  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
        First Name:  <input type="text" name="userName" onChange={(val) => this.setState({userName:val})}></input><br/>
        password :  <input type="password" name="password" onChange={(val) => this.setState({password:val})}></input><br/>
                <input type="submit" value="Login" onClick={this.sendData.bind(this)}></input><br/>
        </p>
      </div>
    );
  }
}

export default App;

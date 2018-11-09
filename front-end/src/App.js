import React, { Component } from 'react';
import Users from './components/Users.js'
import logo from './logo.svg';
import './App.css';
import firebase from 'firebase'
import DisplayData from './components/DisplayData.js';

class App extends Component {
  constructor(props){
      super(props);
      var config = {
          apiKey: "AIzaSyDFNsoyKUiVkw9AYGvQH9HtnEMJ10wk2_A",
          authDomain: "cse110ucsd-da3fc.firebaseapp.com",
          databaseURL: "https://cse110ucsd-da3fc.firebaseio.com",
          projectId: "cse110ucsd-da3fc",
          storageBucket: "cse110ucsd-da3fc.appspot.com",
          messagingSenderId: "735603901433"
      };
      firebase.initializeApp(config);

  }

    render() {
      return (
          < div >
            <Users db={firebase}/>
            <DisplayData db={firebase}/>
          < /div>
      );

  }

}

export default App;

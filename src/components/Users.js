import React, {Component} from 'react';

class Users extends Component {
    constructor(props) {
        super(props);

        this.state = {
            name: '',
            password: ''
        };

        this.firebaseRef = this.props.db.database().ref("Users");
    }

    componentWillUnmount() {
        this.firebaseRef.off();
    }

    pushToFirebase(event) {
        const {name, password} = this.state;
        event.preventDefault();
        this.firebaseRef.child(name).set({name, password});
        this.setState({name: '', password: ''});
    }

    render(){
        return(
            <div>
                <label>User's Name</label>
                <input  value={this.state.name} onChange= {e => this.setState({name: e.target.value})}/>
                <br />
                <label>User's password</label>
                <input  value={this.state.password} onChange= {e => this.setState({password: e.target.value})}/>
                <br />
                <button onClick={this.pushToFirebase.bind(this)}>Submit</button>
            </div>
        );
    }
}

export default Users;
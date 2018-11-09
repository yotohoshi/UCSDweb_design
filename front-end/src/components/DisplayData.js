import React, {Component} from 'react';

class DisplayData extends Component {
    constructor(props) {
        super(props);

        this.state = {
            items: []
        };

        this.firebaseRef = this.props.db.database().ref("Users");
        this.firebaseRef.on('value', dataSnapshot => {
            let items = [];
            dataSnapshot.forEach(childSnapshot => {
                let item = childSnapshot.val();
                item['.key'] = childSnapshot.key;
                items.push(item);
            });
            this.setState({items});
        });
    }

    componentWillUnmount() {
        this.firebaseRef.off();
    }

    render() {
        const records = this.state.items.map(items =>
            <tr key={items.name}>
                <td style={{width: '200px', textAlign: 'center'}}>{items.name}</td>
                <td style={{width: '200px', textAlign: 'center'}}>{items.password}</td>
            </tr>
        );

        return (
            <div style={{paddingTop: '20px'}}>
                <table style={{border: '1px solid black'}}>
                    <thead>
                        <tr>
                            <th>Users' Name</th>
                            <th>Users' Password</th>
                        </tr>
                    </thead>
                    <tbody>
                        {records}
                    </tbody>
                </table>
            </div>
        );
    }
}

export default DisplayData;
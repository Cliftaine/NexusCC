import React, { Component } from 'react'
import { Form,  Button } from 'react-bootstrap';
import axios from 'axios'

export default class Login extends Component {
	constructor(props) {
		super(props)

		this.state = {}
	}

	postLogin(){
		axios.post('login/', {
			email: 'cliftaine1@gmail.com',
			password: '12345'
		}, {withCredentials: true})
		.then(function (response) {
			console.log(response);
		})
		.catch(function (error) {
			console.log(error);
		});
	}

	componentDidMount(){
	}


	render() {
		return(
			<Form>
				<Form.Group className="mb-3" controlId="formBasicEmail">
					<Form.Label>Email address</Form.Label>
					<Form.Control type="l" placeholder="Email" />
				</Form.Group>

				<Form.Group className="mb-3" controlId="formBasicPassword">
					<Form.Label>Password</Form.Label>
					<Form.Control type="password" placeholder="Password" />
				</Form.Group>
				<Button variant="primary" type="Submit">
					Login
				</Button>
			</Form>
		);
	}
}


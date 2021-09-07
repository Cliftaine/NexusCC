import React, { Component } from 'react'
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
		this.postLogin();
	}


	render() {
		return(
			<div>
				Login
			</div>
		);
	}
}


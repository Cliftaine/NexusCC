import React, { Component } from 'react'
import axios from 'axios'

export default class Teams extends Component {
	constructor(props) {
		super(props)

		this.state = {
			teamsData : [],
		}
	}


	postLogin(){
		//axios.defaults.headers.common['Authorization'] = store.getState().session.token;;
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

		axios.get("teams/", {withCredentials: true})
			.then((response) => {
				this.setState({teamsData:response.data})
			})
			.catch(function (error) {
				console.log(error);
		})
	}


	render() {
		return(
			<div>
				{this.state.teamsData.map( item => {
					return <h3> {item.name} </h3>
				})}
			</div>
		);
	}
}


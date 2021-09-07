import React, { Component } from 'react'
import axios from 'axios'

export default class Teams extends Component {
	constructor(props) {
		super(props)

		this.state = {
			teamsData : [],
		}
	}

	componentDidMount(){
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


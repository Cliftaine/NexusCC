import React, { Component } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';

export default class Landing extends Component {
	constructor(props) {
		super(props)

		this.state = {
			teamsData : [],
		}
	}



	//componentDidMount(){
		//axios.get("teams/", {withCredentials: true})
			//.then((response) => {
				//this.setState({teamsData:response.data})
			//})
			//.catch(function (error) {
				//console.log(error);
		//})
	//}


	render() {
		return(
			<div>
				<h3> 
					LANDING
				</h3>
			</div>
		);
	}
}


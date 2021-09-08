import React, { Component } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';

export default class TeamsList extends Component {
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
			<Table striped bordered hover>
				 <thead>
					<tr>
					<th>#</th>
					<th>Nombre del equipo</th>
					<th>Integrantes:</th>
					</tr>
				</thead>
				<tbody>
					<tr>
					  <td>1</td>
					  <td>Mark</td>
					  <td>Mark</td>
					</tr>
				</tbody>
			</Table>
		);
	}
}


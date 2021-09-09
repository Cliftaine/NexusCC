import React, { Component } from 'react';
import axios from 'axios';
import { Table } from 'react-bootstrap';

export default class Accounts extends Component {
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
						<th>Equipo:</th>
						<th>Nombre:</th>
						<th>Inicio:</th>
						<th>Fin:</th>
					</tr>
				</thead>
				<tbody>
					<tr>
						<td>1</td>
						<td>Equipo Perron</td>
						<td>El pepe</td>
						<td>Fecha1</td>
						<td>Fecha2</td>
					</tr>
				</tbody>
			</Table>
		);
	}
}


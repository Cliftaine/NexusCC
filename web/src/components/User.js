
import React, { Component } from 'react'
import { Form,  Button, Row, Col, Container} from 'react-bootstrap';
import axios from 'axios'

export default class User extends Component {
	constructor(props) {
		super(props)

		this.state = {}
	}


	componentDidMount(){
	}


	render() {
		return(

		<Container>
			<Row className="justify-content-md-center">
				<Col md="center">
					<Form  >
						<Form.Group className="mb-3" controlId="formBasicEmail">
							<Form.Label>Email address</Form.Label>
							<Form.Control type="l" placeholder="Email" />
						</Form.Group>

						<Form.Group className="mb-3" controlId="formBasicPassword">
							<Form.Label>Password</Form.Label>
							<Form.Control type="password" placeholder="Password" />
						</Form.Group>
						<Button variant="primary" type="Submit" md="center">
							Login
						</Button>
					</Form>
				</Col>
			</Row>
		</Container>
		);
	}
}


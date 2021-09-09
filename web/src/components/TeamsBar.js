import React, { Component } from 'react';
import {Tab, Nav, Row, Col} from 'react-bootstrap';

export default class NavBar extends Component {
	constructor(props) {
		super(props)

		this.state = {}
	}

	render() {
		return (
			<Tab.Container id="left-tabs-example" defaultActiveKey="first">
				<Row>
					<Col sm={3}>
					  <Nav variant="pills" className="flex-column">
						<Nav.Item>
						  <Nav.Link eventKey="first">Tab 1</Nav.Link>
						</Nav.Item>
						<Nav.Item>
						  <Nav.Link eventKey="second">Tab 2</Nav.Link>
						</Nav.Item>
					  </Nav>
					</Col>
					<Col sm={9}>
					  <Tab.Content>
						<Tab.Pane eventKey="first">
							algo
						</Tab.Pane>
						<Tab.Pane eventKey="second">
							algo
						</Tab.Pane>
					</Tab.Content>
					</Col>
				</Row>
			</Tab.Container>
		)
	}
}

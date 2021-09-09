import React, { Component } from 'react';
import {Nav, Navbar, Container} from 'react-bootstrap';
import {LinkContainer} from 'react-router-bootstrap';
import { faUser } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { connect } from 'react-redux';
import PropTypes from 'prop-types';


export default class NavBar extends Component {
	constructor(props) {
		super(props)
		this.state = {}
	}

	render() {

		const isAuthenticated = true;
		const isSuperUser = true;
		const user= "Pedrito";
		//const { isAuthenticated, isSuperUser, user } = {false, false, "Pedrito"};
	
		const superLinks = (
			<Nav className="me-auto">				
				<LinkContainer to='users'>
					<Nav.Link>Users</Nav.Link>
				</LinkContainer>
				<LinkContainer to='/accounts'>
					<Nav.Link>Cuentas</Nav.Link>
				</LinkContainer>
				<LinkContainer to='/teams'>
					<Nav.Link>Equipos</Nav.Link>
				</LinkContainer>
				<LinkContainer to='/teamsLog'>
					<Nav.Link>Log</Nav.Link>
				</LinkContainer>
			</Nav>
		);
	
		const userLinks = (
			<Nav className="me-auto">
				<LinkContainer to='/profile'>
					<Nav.Link>	Perfil</Nav.Link>
				</LinkContainer>
			</Nav>
		);

		const menuLinks = (
			<Nav>
				<LinkContainer to='/profile'>
					<Nav.Link><FontAwesomeIcon icon={faUser} /></Nav.Link>
				</LinkContainer>
				<LinkContainer to='/logout'>
					<Nav.Link>Salir</Nav.Link>
				</LinkContainer>
			</Nav>
		);

		const loginLinks = (			
			<Nav>
				<LinkContainer to='/login'>
					<Nav.Link>Login</Nav.Link>
				</LinkContainer>
			</Nav>
		);

		return (
			<Navbar collapseOnSelect expand="lg" bg="dark" variant="dark">
				<Container>
					<LinkContainer to='/'>
						<Navbar.Brand>ArkusNexus</Navbar.Brand>
					</LinkContainer>
					<Navbar.Toggle aria-controls="responsive-navbar-nav" />
					<Navbar.Collapse id="responsive-navbar-nav">
						{isSuperUser ? superLinks : userLinks}
						{isAuthenticated ? menuLinks : loginLinks}
					</Navbar.Collapse>
				</Container>
			</Navbar>
		)
	};
}

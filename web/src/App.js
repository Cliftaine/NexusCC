import React, { Fragment } from 'react';
import './App.css';
import { Container } from 'react-bootstrap';
import Login from './components/Login';
import Teams from './components/Teams';
import TeamsList from './components/TeamsList';

const App = () => {
  return (
	<Fragment>
	  <Container>
		<Login/>
		<TeamsList/>
	  </Container>
	  <Teams />
	  <h1>Simon</h1>

	</Fragment>
  );
}

export default App;

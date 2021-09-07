import React, { Fragment } from 'react';
import './App.css';
import Login from './components/Login';
import Teams from './components/Teams';

const App = () => {
  return (
	<Fragment>
	  <Login />
	  <Teams />
	  <h1>Simon</h1>

	</Fragment>
  );
}

export default App;

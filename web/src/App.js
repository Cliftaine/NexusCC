import React from 'react';
import './App.css';
import { Container, Row, Col } from 'react-bootstrap';
import {BrowserRouter as Router, Switch, Route} from 'react-router-dom';
import PrivateRoute from './components/PrivateRoute';

import Login from './components/Login';
import Teams from './components/Teams';
import TeamsLog from './components/TeamsLog';
import Nabvar from './components/NavBar';
import User from './components/User';
import UserList from './components/UserList';
import Accounts from './components/Accounts';
import Landing from './components/Landing';


import { Provider } from 'react-redux';
import store from './store';

const App = () => (
	<Provider store={store}>
		<Router>
			<Nabvar/>
			<Container>
				<Col className="justify-content-md-center">				
					<Row className="justify-content-md-center" md="auto">
						<Switch>
							<PrivateRoute path='/accounts' component={Accounts} exact/>
							<PrivateRoute path='/teamsLog' component={TeamsLog} exact/>
							<PrivateRoute path='/teams' component={Teams} exact/>
							<Route path='/login' component={Login} exact/>
							<PrivateRoute path='/profile' component={User} exact/>
							<PrivateRoute path='/users' component={UserList} exact/>
							<PrivateRoute path='/' component={Landing} exact/>
						</Switch>
					</Row>
				</Col>
			</Container>
		</Router>
	</Provider>
);

export default App;

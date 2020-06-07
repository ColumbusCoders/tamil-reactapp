import React from 'react';
import logo from './logo.svg';
import './App.css';

import {Container,Col,Row} from 'react-bootstrap';
import TopNews from './components/TopNews';
import Navmenu from './components/Navmenu';
import Cinema from './components/Cinema';
import Sports from './components/Sports';
import Business from './components/Business';
import Divine from './components/Divine';
import Politics from './components/Politics';


import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";


function App() {
  return (
    <div>
      <Container fluid>
        <Row>
          <Col> <Navmenu /></Col>
        </Row>
      </Container>
      <Container fluid>
        <Router>
             < Switch>
                  <Route exact path="/">
                      <TopNews />
                  </Route>
                  <Route path="/Politics">
                    <Cinema />
                  </Route>
                  <Route path="/Cinema">
                    <Cinema />
                  </Route>
                  <Route path="/Sports">
                    <Sports />
                  </Route>
                  <Route path="/Business">
                    <Business />
                  </Route>
                  <Route path="/Divine">
                    <Divine />
                  </Route>
             </Switch>
          </Router>
      </Container>

    </div>
  );
}

export default App;

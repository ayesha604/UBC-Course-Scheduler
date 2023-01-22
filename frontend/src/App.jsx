import { useState } from 'react'
import './App.scss'
import Nav from './components/Nav'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

function App() {

  return (
    <div className="App">
      <Nav />

      <Container>
        <Row>
          <Col>

          </Col>
          <Col md={9}>

          </Col>
        </Row>
      </Container>
    </div>
  )
}

export default App

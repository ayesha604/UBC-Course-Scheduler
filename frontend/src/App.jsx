import { useEffect } from 'react'
import './App.scss'
import Nav from './components/Nav'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';

const prefetchCourseURL = 'http://127.0.0.1:5000/valid_courses'

function App() {

  useEffect(() => {
    async function prefetch() {
      try {
        let response = (await fetch(prefetchCourseURL))
        console.log(await response.text())
      } catch(e) {
        console.error("Network request failed")
      }
    }
    prefetch()
  }, [])

  
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

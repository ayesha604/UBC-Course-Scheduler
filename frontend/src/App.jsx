import { useState } from 'react'
import { sendCourses } from './util/api.js'
import './App.scss'
import Nav from './components/Nav'
import Container from 'react-bootstrap/Container'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import TimetableCarousel from './components/TimetableCarousel'

function App() {
  console.log(sendCourses(["CPSC 110"]))

  let timetables = [
    {
      sections: [
        {
          "name": "CPSC 110 103",
          "days": [
            {
              "day": "Mon",
              "times": ["9:30", "11:00"]
            },
            {
              "day": "Wed",
              "times": ["9:30", "11:00"]
            }
          ],
          "location": "West Mall Swing Space",
          "professors": "OLA, OLUWAKEMI",
          "status": ""
        },
        {
          "name": "CHIN 141 T03",
          "days": [
            {
              "day": "Wed",
              "times": ["15:00", "16:00"]
            }
          ],
          "location": "Buchanan",
          "professors": "LEE, LI-JUNG; WANG, HSIANG-NING",
          "status": ""
        }
      ],
      criteriaScore: 9.8
    },
    {
      sections: [
        {
          "name": "ASTR 102 201",
          "days": [
            {
              "day": "Mon",
              "times": ["12:00", "13:00"]
            },
            {
              "day": "Wed",
              "times": ["12:00", "13:00"]
            },
            {
              "day": "Fri",
              "times": ["12:00", "13:00"]
            }
          ],
          "location": "Hennings",
          "professors": "MCIVER, JESSICA",
          "status": ""
        },
        {
          "name": "CPSC 121 201",
          "days": [
            {
              "day": "Tue",
              "times": ["12:30", "14:00"]
            },
            {
              "day": "Thu",
              "times": ["12:30", "14:00"]
            }
          ],
          "location": "West Mall Swing Space",
          "professors": "TIEN, GEOFFREY",
          "status": ""
        }
      ],
      criteriaScore: 4.3
    }
  ]

  return (
    <div className="App">
      <Nav />

      <Container fluid>
        <Row>
          <Col className="sidebar">
            <Container>
              Text
            </Container>
          </Col>
          <Col md={9}>
            {timetables && 
              <TimetableCarousel timetables={timetables} />
            }
          </Col>
        </Row>
      </Container>
    </div>
  )
}

export default App

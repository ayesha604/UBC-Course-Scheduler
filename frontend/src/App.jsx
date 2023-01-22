import { useState, useEffect } from 'react'
import { sendCourses } from './util/api.js'
import './App.scss'
import Sidebar from './components/Sidebar'
import Container from 'react-bootstrap/Container'
import Nav from './components/Nav'
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import TimetableCarousel from './components/TimetableCarousel'
import TimetablePlaceholder from './components/TimetablePlaceholder.jsx'


const prefetchCourseURL = 'http://127.0.0.1:5000/valid_courses'

function App() {
  const [loading, setLoading] = useState(false)
  const [timetables, setTimetables] = useState()
  // let timetables = [
  //   {
  //     sections: [
  //       {
  //         "name": "CPSC 110 103",
  //         "days": [
  //           {
  //             "day": "Mon",
  //             "times": ["9:30", "11:00"]
  //           },
  //           {
  //             "day": "Wed",
  //             "times": ["9:30", "11:00"]
  //           }
  //         ],
  //         "location": "West Mall Swing Space",
  //         "professors": "OLA, OLUWAKEMI",
  //         "status": ""
  //       },
  //       {
  //         "name": "CHIN 141 T03",
  //         "days": [
  //           {
  //             "day": "Wed",
  //             "times": ["15:00", "16:00"]
  //           }
  //         ],
  //         "location": "Buchanan",
  //         "professors": "LEE, LI-JUNG; WANG, HSIANG-NING",
  //         "status": ""
  //       }
  //     ],
  //     criteriaScore: 9.8
  //   },
  //   {
  //     sections: [
  //       {
  //         "name": "ASTR 102 201",
  //         "days": [
  //           {
  //             "day": "Mon",
  //             "times": ["12:00", "13:00"]
  //           },
  //           {
  //             "day": "Wed",
  //             "times": ["12:00", "13:00"]
  //           },
  //           {
  //             "day": "Fri",
  //             "times": ["12:00", "13:00"]
  //           }
  //         ],
  //         "location": "Hennings",
  //         "professors": "MCIVER, JESSICA",
  //         "status": ""
  //       },
  //       {
  //         "name": "CPSC 121 201",
  //         "days": [
  //           {
  //             "day": "Tue",
  //             "times": ["12:30", "14:00"]
  //           },
  //           {
  //             "day": "Thu",
  //             "times": ["12:30", "14:00"]
  //           }
  //         ],
  //         "location": "West Mall Swing Space",
  //         "professors": "TIEN, GEOFFREY",
  //         "status": ""
  //       }
  //     ],
  //     criteriaScore: 4.3
  //   }
  // ]

  async function handleGetTimetables(courses, term) {
    setLoading(true)
    setTimetables((await sendCourses(courses, term)).timetables)
    setLoading(false)
  }

  const [courseData, setCourseData] = useState()
  useEffect(() => {
    async function prefetch() {
      try {
        let response = (await fetch(prefetchCourseURL))
        setCourseData(await response.json())
      } catch(e) {
        console.error("Network request failed")
      }
    }
    prefetch()
  }, [])

  
  return (
    <div className="App">
      <Nav />

      <Container fluid>
        <Row>
          <Col className="sidebar">
            <Container>
              <Sidebar handleSubmit={handleGetTimetables} courseData={courseData} />
            </Container>
          </Col>
          <Col md={9}>
            {timetables && timetables.length > 0 && !loading &&
              <TimetableCarousel timetables={timetables} />
            }
            {loading &&
              <TimetablePlaceholder />
            }
            {!timetables && !loading &&
              <p class="inactive">Please enter your desired courses on the left.</p>
            }
          </Col>
        </Row>
      </Container>
    </div>
  )
}

export default App

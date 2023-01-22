import React, { useState, useEffect, useRef } from 'react'
import Timetable from './Timetable'
import Container from 'react-bootstrap/Container'
import { IoTriangleSharp } from 'react-icons/io5'
import './TimeTableCarousel.scss'

export default function TimetableCarousel() {
    const [currentTimetable, setCurrentTimetable] = useState(0)

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

    function handleNextTimetable() {
        if(currentTimetable !== timetables.length - 1) {
            setCurrentTimetable(currentTimetable + 1)
        }
    }
    function handlePrevTimetable() {
        if(currentTimetable !== 0) {
            setCurrentTimetable(currentTimetable - 1)
        }
    }

    return (
        <Container>
            <div className="carousel">
                <button onClick={handlePrevTimetable} className="btn-round left" disabled={currentTimetable === 0}>
                    <IoTriangleSharp />
                </button>
                <div >
                    <Timetable sections={timetables[currentTimetable].sections} criteriaScore={timetables[currentTimetable].criteriaScore} num={currentTimetable} />
                </div>
                
                <button onClick={handleNextTimetable} className="btn-round right" disabled={currentTimetable === timetables.length - 1}>
                    <IoTriangleSharp />
                </button>
            </div>
                
            
        </Container>
    )
}
import React, { useState, useEffect, useRef } from 'react'
import Timetable from './Timetable'
import Container from 'react-bootstrap/Container'
import { IoTriangleSharp } from 'react-icons/io5'
import './TimeTableCarousel.scss'

export default function TimetableCarousel({ timetables }) {
    const [currentTimetable, setCurrentTimetable] = useState(0)
    const [animDirection, setAnimDirection] = useState("anim-left")

    function handleNextTimetable() {
        if(currentTimetable !== timetables.length - 1) {
            setCurrentTimetable(currentTimetable + 1)
            setAnimDirection("anim-right")
        }
    }
    function handlePrevTimetable() {
        if(currentTimetable !== 0) {
            setCurrentTimetable(currentTimetable - 1)
            setAnimDirection("anim-left")
        }
    }

    return (
        <Container fluid>
            <div className="carousel">
                <button onClick={handlePrevTimetable} className="btn-round left" disabled={currentTimetable === 0}>
                    <IoTriangleSharp />
                </button>
                <div className={animDirection} key={currentTimetable}>
                    <Timetable sections={timetables[currentTimetable].sections}
                                criteriaScore={timetables[currentTimetable].criteriaScore}
                                num={currentTimetable} />
                </div>
                
                <button onClick={handleNextTimetable} className="btn-round right" disabled={currentTimetable === timetables.length - 1}>
                    <IoTriangleSharp />
                </button>
            </div>
                
            
        </Container>
    )
}
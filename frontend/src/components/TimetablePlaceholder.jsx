import React, { useState } from 'react'
import OverlayTrigger from 'react-bootstrap/OverlayTrigger'
import Popover from 'react-bootstrap/Popover'
import './Timetable.scss'

const weekdaysAbbrv = ["Mon", "Tue", "Wed", "Thu", "Fri"]
const weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
// blue, rust, light blue, purple, green, magenta
const sectionColors = ["#2853C3", "#A72323", "#2D8DB7", "#7E259D", "#369D25", "#B727BA"]

export default function TimetablePlaceholder() {

    return (
        <div className="container" style={{paddingLeft: "5.5em", paddingRight: "5.5em"}}>
            <div>
                <h1 style={{visibility: "hidden"}}>Timetable</h1>
                <p style={{ visibility: "hidden" }}>Criteria score:</p>
                <table className="skeleton">
                    <thead>
                        <tr>
                            <th className="times"></th>
                            {weekdays.map((e, i) => <th key={i}><span style={{visibility: "hidden"}}>Text</span></th>)}
                        </tr>
                    </thead>
                    <tbody>
                        {[...Array(26)].map((e, i) => { return (
                            <tr key={i}>
                                <td className="time"></td>
                                <td className="time"></td>
                                <td className="time"></td>
                                <td className="time"></td>
                                <td className="time"></td>
                                <td className="time"></td>
                            </tr>
                        )})}
                    </tbody>
                </table>
            </div>
        </div>
    )
}
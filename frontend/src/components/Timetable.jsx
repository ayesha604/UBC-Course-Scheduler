import React, { useState } from 'react'
import Container from 'react-bootstrap/Container'
import OverlayTrigger from 'react-bootstrap/OverlayTrigger'
import Popover from 'react-bootstrap/Popover'
import './Timetable.scss'

let weekdaysAbbrv = ["Mon", "Tue", "Wed", "Thu", "Fri"]
let weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]


function makeTimes() {
    let times = []
    for (let i = 8; i <= 20; i++) {
        const hour = String(i).padStart(2, '0')
        times.push(hour + ":00")
        if (i != 20) times.push(hour + ":30")
    }
    return times
}

function getDuration(startTime, endTime) {
            let startHour = parseInt(startTime.split(":")[0])
            let startMinute = parseInt(startTime.split(":")[1])
            let totalStartMinutes = startHour * 60 + startMinute

            let endHour = parseInt(endTime.split(":")[0])
            let endMinute = parseInt(endTime.split(":")[1])
            let totalEndMinutes = endHour * 60 + endMinute

            let duration = totalEndMinutes - totalStartMinutes

            return duration
}

function getDaysFilledWith(sections, times) {
    let daysWithTimes = weekdaysAbbrv.map(() => Array(26).fill().map((e) => {return {index: -1}}))

    // let sectionsTimeInfo = getSectionsTimeInfo(sections, times)
    sections.forEach((section, i) => {
        section.days.forEach((day) => {
            let startHour = parseInt(day["times"][0].split(":")[0])
            let startMinute = parseInt(day["times"][0].split(":")[1])

            let duration = getDuration(day["times"][0], day["times"][1])

            let startTimeIndex = times.indexOf(String(startHour).padStart(2, "0") + ":" +
                                String(startMinute).padStart(2, "0"))
            let rowSpan = (duration / 60) * 2


            daysWithTimes[weekdaysAbbrv.indexOf(day.day)][startTimeIndex].index = i
            daysWithTimes[weekdaysAbbrv.indexOf(day.day)][startTimeIndex].rowSpan = rowSpan

            
            for(let j = startTimeIndex+1; j < startTimeIndex+rowSpan; j++) {
                daysWithTimes[weekdaysAbbrv.indexOf(day.day)][j].index = -2
            }
        })
    })

    return daysWithTimes
}

export default function Timetable() {
    const [criteriaScore, setCriteriaScore] = useState(9.8)
    let criteriaScoreColor = criteriaScore > 6.6 ? "score-hi" : 
                            criteriaScore > 3.3 ? "score-med" : "score-low"

    let times = makeTimes()

    let sections = [
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
                },
                {
                    "day": "Fri",
                    "times": ["9:30", "11:00"]
                }
            ],
            "location": "West Mall Swing Space",
            "professors": "OLA, OLUWAKEMI",
            "states": ""
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
    ]
    
    let daysFilledWith = getDaysFilledWith(sections, times)
    return (
        <div>
            <button className="btn-round">Left</button>
            <h1>Timetable 1</h1>
            <p>Criteria score: <span className={criteriaScoreColor}>{criteriaScore}</span></p>
            <Container>
                <table>
                    <thead>
                        <tr>
                            <th class="times"></th>
                            {weekdays.map((e) => <th>{e}</th>)}
                        </tr>
                    </thead>
                    <tbody>
                        {times.map((time, i) => { return (
                            <tr>
                                {i % 2 == 0 && 
                                    <td className="time-text">{time}</td>
                                }
                                {i % 2 == 1 &&
                                    <td className="time"></td>
                                }
                                {daysFilledWith.map((day) => {
                                    if(day[i].index === -1) {
                                        return (<td></td>)
                                    } else if(day[i].index === -2) {
                                        return(<></>)
                                    } else {
                                        return (
                                            <OverlayTrigger trigger="click" placement="right" overlay={
                                                <Popover body>
                                                    <h3 className="popover-heading">{sections[day[i].index]["name"]}</h3>
                                                    <p className="popover-line"><span className="semibold">Days:</span> {sections[day[i].index]["days"].map((day) => day.day).join(", ")}</p>
                                                    <p className="popover-line"><span className="semibold">Location:</span> {sections[day[i].index]["location"]}</p>
                                                </Popover>}>
                                                <td className="section-slot" rowSpan={day[i].rowSpan} style={{ backgroundColor: "#274082"}}>
                                                    <p className="slot-title">{sections[day[i].index]["name"]}</p>
                                                    <p className="slot-subtitle">{sections[day[i].index]["location"]}</p>
                                                </td>
                                            </OverlayTrigger>
                                        )
                                    }
                                })}
                                
                            </tr>
                        )})}
                    </tbody>
                </table>
                
            </Container>
        </div>
    )
}
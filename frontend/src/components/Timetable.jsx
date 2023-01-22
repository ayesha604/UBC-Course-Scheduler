import React, { useState } from 'react'
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

export default function Timetable({ sections, criteriaScore, num }) {
    let criteriaScoreColor = criteriaScore > 6.6 ? "score-hi" : 
                            criteriaScore > 3.3 ? "score-med" : "score-low"

    let times = makeTimes()
    let daysFilledWith = getDaysFilledWith(sections, times)

    return (
        <div className="container">
            <div>
                <h1>Timetable {num + 1}</h1>
                <p>Criteria score: <span className={criteriaScoreColor}>{criteriaScore}</span></p>
                <table>
                    <thead>
                        <tr>
                            <th className="times"></th>
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
                                {daysFilledWith.map((day, j) => {
                                    if(day[i].index === -1) {
                                        return (<td></td>)
                                    } else if(day[i].index === -2) {
                                        return(<></>)
                                    } else {
                                        return (
                                            <OverlayTrigger trigger="click" placement="right" overlay={
                                                <Popover body>
                                                    <h3 className="popover-heading">{sections[day[i].index]["name"]}</h3>
                                                    <p className="popover-line"><span className="semibold">Location:</span> {sections[day[i].index]["location"]}</p>
                                                    <p className="popover-line"><span className="semibold">Time:</span> {sections[day[i].index]["days"].find((e) => e.day === weekdaysAbbrv[j]).times.join("-")}</p>
                                                    <p className="popover-line"><span className="semibold">Days:</span> {sections[day[i].index]["days"].map((e) => e.day).join(", ")}</p>
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
            </div>
        </div>
    )
}
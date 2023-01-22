import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'
import './Nav.scss'

export default function Nav() {

    return (
        <Navbar bg="light">
            <Container fluid>
                <Navbar.Brand as="div">
                    <h1 className="logo">
                        UBC Course Scheduler
                    </h1>
                </Navbar.Brand>
            </Container>
        </Navbar>
    )
}
import React from 'react'
import Navbar from 'react-bootstrap/Navbar'
import Container from 'react-bootstrap/Container'
import './Nav.scss'

export default function Nav() {

    return (
        <Navbar bg="light">
            <Container>
                <Navbar.Brand as="div">
                    <h1 class="logo">
                        UBC Course Scheduler
                    </h1>
                </Navbar.Brand>
            </Container>
        </Navbar>
    )
}
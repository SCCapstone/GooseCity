import React from 'react'
import {Container, Nav, Navbar, NavDropdown} from "react-bootstrap";
import './header.css';

function TableToolbar() {

  return (
    <Navbar collapseOnSelect expand="lg" bg="light" variant="light" sticky="top" style={{paddingLeft : 0, paddingRight : 0}}>
      <Container className="mx-auto" style={{paddingLeft : 0, paddingRight : 0}}>
      <Navbar.Brand href="/">
          <b>GooseCity</b>
      </Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link href="#/TempView">Features</Nav.Link>
          <Nav.Link href="#/TempView">Pricing</Nav.Link>
          <NavDropdown title="More" id="collasible-nav-dropdown">
            <NavDropdown.Item href="#/TempView">Action</NavDropdown.Item>
            <NavDropdown.Item href="#/TempView">Another action</NavDropdown.Item>
            <NavDropdown.Item href="#/TempView">Something</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="#/TempView">Separated link</NavDropdown.Item>
          </NavDropdown>
        </Nav>
        <div>
        </div>
        <Nav>
          <Nav.Link href="#/LoginView">log in </Nav.Link>
          <Nav.Link eventKey={2} href="#/RegisterView">
            register
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
      </Container>
    </Navbar>
  )
}



export default TableToolbar
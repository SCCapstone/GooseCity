import React from 'react'
import {Container, Nav, Navbar, NavDropdown} from "react-bootstrap";
import './style.css';

function TableToolbar() {

  return (
    <Navbar collapseOnSelect expand="lg" bg="light" variant="light" sticky="top">
      <Container>
      <Navbar.Brand href="#home">React-Bootstrap</Navbar.Brand>
      <Navbar.Toggle aria-controls="responsive-navbar-nav" />
      <Navbar.Collapse id="responsive-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link href="#features">Features</Nav.Link>
          <Nav.Link href="#pricing">Pricing</Nav.Link>
          <NavDropdown title="Dropdown" id="collasible-nav-dropdown">
            <NavDropdown.Item href="#action/3.1">Action</NavDropdown.Item>
            <NavDropdown.Item href="#action/3.2">Another action</NavDropdown.Item>
            <NavDropdown.Item href="#action/3.3">Something</NavDropdown.Item>
            <NavDropdown.Divider />
            <NavDropdown.Item href="#action/3.4">Separated link</NavDropdown.Item>
          </NavDropdown>
        </Nav>
        <div>
        </div>
        <Nav>
          <Nav.Link href="#deets">log in </Nav.Link>
          <Nav.Link eventKey={2} href="#memes">
            register
          </Nav.Link>
        </Nav>
      </Navbar.Collapse>
      </Container>
    </Navbar>
  )
}



export default TableToolbar
import React, {Component} from 'react'
import {Container, Nav, Navbar, NavDropdown} from "react-bootstrap";
import './header.css';

    function accountName() {
    let ret;
    if(window.localStorage.token === undefined){
        ret = "Account";
    }else
        ret = window.localStorage.token.replace(/^\"|\"$/g,'');
    return ret;
    }

class TableToolbar extends Component{
    constructor (props) {
      super(props)
    }

    logout = (props)=> {
        window.localStorage.removeItem('token');
        window.location.reload(false);
        //this.props.history.push('/');
    }

    render() {
        return (
            <Navbar collapseOnSelect expand="lg" bg="light" variant="light" sticky="top" style={{paddingLeft : 0, paddingRight : 0}}>
              <Container className="mx-auto" style={{paddingLeft : 0, paddingRight : 0}}>
              <Navbar.Brand href="#">
                  <b>GooseCity</b>
              </Navbar.Brand>
              <Navbar.Toggle aria-controls="responsive-navbar-nav" />
              <Navbar.Collapse id="responsive-navbar-nav">
                <Nav className="me-auto">
                  <Nav.Link href="#/TempView">Holiday deals</Nav.Link>
                  <Nav.Link href="#/TempView">Recommendations</Nav.Link>
                  <NavDropdown title="All" id="collasible-nav-dropdown">
                    <NavDropdown.Item href="#/TempView">Best Sellers</NavDropdown.Item>
                    <NavDropdown.Item href="#/TempView">New Releases</NavDropdown.Item>
                    {/*<NavDropdown.Divider />*/}
                    <NavDropdown.Item href="#/TempView">Most Wished For</NavDropdown.Item>
                  </NavDropdown>
                </Nav>
                <div>
                </div>
                  <Nav >
                    <NavDropdown title={accountName()} id="collasible-nav-dropdown">
                        {
                            window.localStorage.token === undefined ?
                                <NavDropdown.Item href="#/LoginView" >log in</NavDropdown.Item> : null
                        }
                        {
                            window.localStorage.token === undefined ?
                                <NavDropdown.Item href="#/RegisterView">register</NavDropdown.Item> : null
                        }
                        {
                            window.localStorage.token === undefined ?
                                null : <NavDropdown.Item href="#/TempView">My Account</NavDropdown.Item>
                        }
                        {
                            window.localStorage.token === undefined ?
                                null : <NavDropdown.Item href="#/TempView">My Cart</NavDropdown.Item>
                        }
                    <NavDropdown.Item href="#/LoginView" onClick={this.logout}>log out</NavDropdown.Item>
                  </NavDropdown>
                </Nav>
              </Navbar.Collapse>
              </Container>
            </Navbar>
      )
    }

}

export default TableToolbar
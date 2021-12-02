import React, { Component, useState } from "react";
import {Card, Col, Container, DropdownButton, Form, Nav, NavDropdown, Row} from "react-bootstrap";
import axios from "axios";
import TableToolbar from "../header/header";
import {Button, Dropdown} from "bootstrap";


class ShoppingTable extends Component {
  constructor(props) {
    super(props);
    this.state = {
      todoList: [],
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    let data = new FormData();
    if(window.localStorage.token !== undefined ){
        data.append("token", window.localStorage.token.replace(/^\"|\"$/g,''));
        axios
          .post("http://localhost:8000/getshoppingcard/",data)
          .then((res) => this.setState({ todoList: res.data }))
          .catch((err) => console.log(err));
    }
    else {
        window.history.go(-1);
    }
  };


  handleDeleteFromCard = (item) => {
        let data = new FormData();
        let token = window.localStorage.token.replace(/^\"|\"$/g,'');
        data.append("token", token);
        data.append("id", item.id);
        axios.post("http://localhost:8000/rmcart/",data).then(res => {
            console.log("rm"+item.id);
            this.refreshList();
        });
  };


  Subtotal = () => {
    let subtotal = 0;
    for (let i=0;i<this.state.todoList.length;i++){
      subtotal += parseFloat(this.state.todoList[i].prices.match(/\d+(.\d+)?/g)[0]);
    }
    console.log(subtotal)
    subtotal = subtotal.toFixed(2)
    return subtotal;
  }

  renderItems = () => {
    console.log(this.state.todoList);
    const newItems = this.state.todoList
    if(newItems.length === 0){
        return (
            <Container>
                <Row className="justify-content-md-center">
                  <h5 className="text-center m-auto">
                    Your Cart is empty.
                  </h5>

                  <h6 className="text-center m-auto">
                    Check your Saved for later items below or <Nav.Link href="#/">continue shopping.</Nav.Link>
                  </h6>
                </Row>
            </Container>
        )
    }
    return  (
      <Container>
        <Row className="justify-content-md-center">
          { newItems.map((item) => (
            <Card>
              <Row>
                <Col>
                  <img className="card-img-fluid" src={item.image} alt="..." style={{width: 150, height: 150}}/>
                </Col>
                <Col xs lg="4">
                  <h4 className="text-center m-auto" >{item.product_name}</h4>
                </Col>
                <Col>
                  <h5 className="text-center m-auto">{"$"+item.prices.match(/\d+(.\d+)?/g)[0]}</h5>
                </Col>
                <Col>
                  <NavDropdown className="text-center m-auto" title={`Qty: 1`} id="collasible-nav-dropdown">
                    <NavDropdown.Item onClick={()=>this.handleDeleteFromCard(item)}>Delete</NavDropdown.Item>
                      <NavDropdown.Divider />
                    <NavDropdown.Item href="#/TempView">Checkout</NavDropdown.Item>
                  </NavDropdown>
                </Col>
              </Row>
            </Card>
          ))
        }
        </Row>
        <Card>
            <Row>
              <Col xs lg = "8"/>
              <Col>
                <h5 className="text-center" md="auto">Subtotal: {this.Subtotal()}</h5>
              </Col>
              <Col>
                  <NavDropdown.Item href="#/TempView">Proceed to checkout</NavDropdown.Item>
              </Col>
            </Row>

        </Card>
      </Container>
    );
  };

  render() {
    return (
        <main>
          {this.renderItems()}
        </main>
    );
  }
}

export default ShoppingTable;
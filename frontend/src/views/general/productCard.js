import React, { Component, useState } from "react";
import Modal from "../../components/Modal";
import {Card, Col, Form, Row} from "react-bootstrap";
import { Link } from "react-router-dom";
import axios from "axios";
import TableToolbar from "../header/header";
import {Button} from "bootstrap";


class ProductCard extends Component {

  constructor(props) {
    super(props);
    this.state = {
      disable: false,
      viewCompleted: true,
      todoList: [],
      modal: false,
      activeItem: {
        product_name: "",
        description: "",
        link: "",
        image: "",
        condition: "",
        prices: 0,
        free_returns: true,
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("http://localhost:8000/api/todos/")
      .then((res) => this.setState({ todoList: res.data }))
      .catch((err) => console.log(err));
  };

  toggle = () => {
    this.setState({ modal: !this.state.modal });
  };

  handleSubmit = (item) => {
    //this.toggle();

    if (item.id) {
      item.free_returns = !item.free_returns;
      axios
        .put(`http://localhost:8000/api/todos/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axios
      .post("http://localhost:8000/api/todos/", item)
      .then((res) => this.refreshList());
  };
  handleDeleteFromCard = (item) => {
    item.free_returns = !item.free_returns;
    axios
        .put(`http://localhost:8000/api/todos/${item.id}/`, item)
        .then((res) => this.refreshList());
  };
  handleDelete = (item) => {
    let baseurl = 'http://localhost:8000/api/todos/';
    axios
      .delete(baseurl+item.id+'/')
      .then((res) => this.refreshList());
  };

  createItem = () => {
    const item = {
      product_name: "",
      description: "",
      link: "",
      image: "",
      condition: "",
      prices: 0,
      free_returns: true,
    };

    this.setState({ product_name: item, modal: !this.state.modal });
  };

  displayCompleted = (status) => {
    if (status) {
      this.setState({ disable: !this.state.disable })
      return this.setState({ viewCompleted: true });
    }
    this.setState({ disable: !this.state.disable })
    return this.setState({ viewCompleted: false });
  };

  renderTabList = () => {
    return (
      <div className="col-md-12 mb-4">
        <a type="button" className="btn-floating teal"> <i className="fas fa-arrows-alt" aria-hidden="true"> </i></a>
        <a type="button" className="btn-floating light-green"> <i className="far fa-hand-point-right" aria-hidden="true"> </i></a>
      </div>
    );
  };



  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList.filter(
      (item) => item.free_returns === viewCompleted
    );
    // const newItems = this.state.todoList;
    return  (
      <Row  className="g-4" >
      { newItems.slice(0,10).map((item) => (
      <Col>
        <Card style={{ height : '27rem', width : '18rem'}}>
          <img class="card-img-fluid" src={item.image} alt="..."
          />

          <Card.Body>
            <Card.Title class="border-top">{item.product_name}</Card.Title>
            {/*<Card.Text class="border-top">*/}
            {/*  This is a longer card with supporting text*/}
            {/*</Card.Text>*/}
            <Card.Text class="border-top">
              {"$"+item.prices.match(/\d+(.\d+)?/g)[0]}
            </Card.Text>
            <Card.Text >
              <Link
                 to={{
                pathname: "/product/"+item.id,}}
              >
                View Details
              </Link>
            </Card.Text>
          </Card.Body>
        </Card>
      </Col>
  ))
      }
    </Row>
    );
  };

  render() {
    return (
        <main className="product_table">
          {this.renderTabList()}
          <ul className="list-group list-group-flush border-top-0">
            {this.renderItems()}
          </ul>
        </main>
    );
  }
}

export default ProductCard;
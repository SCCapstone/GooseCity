import React, { Component, useState } from "react";
import Modal from "./components/Modal";
import {Card, Form} from "react-bootstrap";
import { Link } from "react-router-dom";
import axios from "axios";
import {Button} from "bootstrap";

class App extends Component {

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
    axios
      .delete(`http://localhost:8000/api/todos/${item.id}/`)
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
      <div className="nav nav-tabs">
        <span
          onClick={() => this.displayCompleted(true)}
          className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
        >
          Product List
        </span>
        <span
          onClick={() => this.displayCompleted(false)}
          className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
        >
          Card
        </span>
      </div>
    );
  };

  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList.filter(
      (item) => item.free_returns === viewCompleted
    );
    // const newItems = this.state.todoList;
    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.description}
        >
        </span>
        <span>
          <Card style={{ width: '23rem' }}>
          <Card.Img variant="top" src={item.image} />
          <Card.Body>
            <Card.Title> {item.product_name} </Card.Title>
            <Card.Text>
              Some quick example text to build on the card title and make up the bulk of
              the card's content.
            </Card.Text>
            <Card.Text>
              {item.prices}
              {item.id}
            </Card.Text>
            </Card.Body>
          </Card>
        </span>
        <span>
          <Link
            className="btn btn-primary" to={{
              pathname: "/product/"+item.id,}}
          >
            View
          </Link>
          <button
            className="btn btn-success"
            disabled={this.state.disable}
            onClick={() => this.handleSubmit(item)}
          >
            Add to Card
          </button>
          <button
            className="btn btn-danger"
             disabled={!this.state.disable}
            onClick={() => this.handleDeleteFromCard(item)}
          >
            Delete From Card
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-white text-uppercase text-center my-4">Todo app</h1>
        <div className="row">
          <div className="col-md-12 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Login
                </button>{'   '}
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  register
                </button>
              </div>
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.modal ? (
          <Modal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}
      </main>
    );
  }
}

export default App;
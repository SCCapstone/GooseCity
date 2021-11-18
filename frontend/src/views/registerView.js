import React, { Component, useState } from "react";
import { Form, Button, FloatingLabel, Alert } from "react-bootstrap";
import axios from "axios";
import TableToolbar from "./header/header";

class RegisterView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      pwd: "",
      confirmedPwd: "",
      display: "none",
    };
  }

  handelEmail = (e) => {
    this.setState({
      email: e.target.value,
    });
  };
  handelPwd = (e) => {
    this.setState({
      pwd: e.target.value,
    });
  };

  handelConfirmedPwd = (e) => {
    if (this.state.pwd !== e.target.value) {
      this.setState({
        display: "block",
        confirmedPwd: e.target.value,
      });
    } else {
      this.setState({
        display: "none",
        confirmedPwd: e.target.value,
      });
    }
  };
  handelSubmit = (e) => {
    e.preventDefault();
    if (this.state.pwd !== this.state.confirmedPwd) {
      this.setState({
        display: "block",
      });
    } else {
      this.setState({
        display: "none",
      });
    }

    let data = new FormData();
    data.append("email", this.state.email);
    data.append("password", this.state.pwd);
    axios.post(`http://localhost:8000/apiv2/register`, data).then((res) => {
      console.log("res=>", res);
    });

    console.log(this.state.email, this.state.pwd);
  };

  render() {
    return (
      <main>
        <header>
          {TableToolbar()}
        </header>
        <Form
            onSubmit={this.handelSubmit}
            style={{ width: "300px", margin: "0 auto", marginTop: "100px" }}
        >
          <h1 style={{ margin: "10px 80px" }}>Sign Up</h1>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control
                type="email"
                placeholder="Enter email"
                value={this.state.email}
                onChange={this.handelEmail}
            />
            <Form.Text className="text-muted">
              We'll never share your email with anyone else.
            </Form.Text>
          </Form.Group>

          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control
                type="password"
                placeholder="Password"
                value={this.state.pwd}
                onChange={this.handelPwd}
            />
          </Form.Group>
          <Form.Group className="mb-3" controlId="formBasicPassword">
            <Form.Label>Confirm Password</Form.Label>
            <Form.Control
                type="password"
                placeholder="Password"
                value={this.state.confirmedPwd}
                onChange={this.handelConfirmedPwd}
            />
          </Form.Group>
          <Alert variant="danger" style={{ display: this.state.display }}>
            Inconsistent with the previous one
          </Alert>
          <Form.Group className="mb-3" controlId="formBasicCheckbox">
            <Form.Check type="checkbox" label="Remember me" />
          </Form.Group>
          <br />
          <Button
              variant="success"
              type="submit"
              style={{ width: "200px", margin: "5px 50px" }}
          >
            sign up
          </Button>
        </Form>
      </main>
    );
  }
}
export default RegisterView;

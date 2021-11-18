import React, { Component, useState } from "react";
import { Form, Button,Nav } from "react-bootstrap";
import axios from "axios";
import TableToolbar from "./header/header";


export default function LoginView () {

  const [username, setUserName] = useState();
  const [password, setPassword] = useState();

  const handelSubmit = async  e => {
    e.preventDefault();

    let data = new FormData();
    data.append("email", username);
    data.append("password", password);
    console.log(data);
    axios.post(`http://localhost:8000/apiv2/login`, data).then((res) => {
      console.log("res=>", res);
      localStorage.setItem('token', JSON.stringify(res.data.token));
      window.location.reload(false);
    });
  };
    console.log(window.localStorage.token === undefined);
    return (
      <main>
        <header>
          {TableToolbar()}
        </header>
        <Form
            onSubmit={handelSubmit}
            style={{ width: "300px", margin: "0 auto", marginTop: "100px" }}
        >
          <h1 style={{ margin: "10px 80px" }}>Log in</h1>
          <Form.Group className="mb-3" controlId="formBasicEmail">
            <Form.Label>Email address</Form.Label>
            <Form.Control
                type="email"
                placeholder="Enter email"
                onChange={e => setUserName(e.target.value)}
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
                onChange={e => setPassword(e.target.value)}
            />
          </Form.Group>
          <br />
          <Button
              variant="primary"
              type="submit"
              style={{ width: "200px", margin: "10px 50px" }}
          >
            Login
          </Button>
          <br />
          <Nav.Link href="#/RegisterView">
            <Button
                variant="success"
                style={{ width: "200px", margin: "5px 35px" }}
            >
              Sign up
            </Button>
          </Nav.Link>
        </Form>
      </main>
    );
}



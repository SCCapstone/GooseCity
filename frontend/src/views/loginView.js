import React, { Component, useState } from "react";
import { Form, Button, Nav, Toast } from "react-bootstrap";
import axios from "axios";
import TableToolbar from "./header/header";

class LoginView extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      pwd: "",
      showSuccess:false,
      showError:false,
      errorMsg:"",
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

  handelSubmit = (e) => {
    e.preventDefault();

    let data = new FormData();
    data.append("email", this.state.email);
    data.append("password", this.state.pwd);
    axios.post(`http://localhost:8000/apiv2/login`, data).then((res) => {
      console.log("res=>", res);
      if(res["data"]["errorMsg"]==="success"){
        this.setState({
          showSuccess:true,
          showError:false,
        })
      }else{
        this.setState({
          showError:true,
          showSuccess:false,
          errorMsg:"Error email or password!"
        })
      }
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
         <Toast
             className="d-inline-block m-1"
             bg="success"
             show={this.state.showSuccess}
         >
           <Toast.Header>
             <img
                 src="holder.js/20x20?text=%20"
                 className="rounded me-2"
                 alt=""
             />
             <strong className="me-auto">City App</strong>
             <small>login</small>
           </Toast.Header>
           <Toast.Body className="text-white">
             Login Successfully!
           </Toast.Body>
         </Toast>

         <Toast
             className="d-inline-block m-1"
             bg="danger"
             show={this.state.showError}
         >
           <Toast.Header>
             <img
                 src="holder.js/20x20?text=%20"
                 className="rounded me-2"
                 alt=""
             />
             <strong className="me-auto">City App</strong>
             <small>login</small>
           </Toast.Header>
           <Toast.Body className="text-white">
             {this.state.errorMsg}
           </Toast.Body>
         </Toast>
         <h1 style={{ margin: "10px 80px" }}>Log in</h1>
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
}
export default LoginView;

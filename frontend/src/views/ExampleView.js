// import React, { Component, useState } from "react";
// import Modal from "./components/Modal";
// import {Card, Form} from "react-bootstrap";
// import { Link } from "react-router-dom";
// import axios from "axios";
// import * as PropTypes from "prop-types";
//
//
// class Text extends Component {
//   render() {
//     return null;
//   }
// }
//
// Text.propTypes = {
//   fontSize: PropTypes.string,
//   ml: PropTypes.number,
//   children: PropTypes.node
// };
//
// class Example extends Component {
//   constructor(props) {
//     super(props);
//     this.state = {
//       viewCompleted: true,
//       todoList: [],
//       modal: false,
//       activeItem: {
//         product_name: "",
//         description: "",
//         link: "",
//         image: "",
//         condition: "",
//         prices: 0,
//         free_returns: true,
//       },
//     };
//   }
//
//   componentDidMount() {
//     this.refreshList();
//   }
//
//   refreshList = () => {
//     console.log("props\n"+this.props);
//     axios
//       .get("http://localhost:8000/api/todos/")
//       .then((res) => console.log(res))
//       .catch((err) => console.log(err));
//   };
//
//   toggle = () => {
//     this.setState({ modal: !this.state.modal });
//   };
//
//
//   render() {
//     return (
//           <Text ml={1} fontSize="sm">
//           <b>4.84</b> (190)
//         </Text>
//     );
//   }
// }
//
// export default Example;
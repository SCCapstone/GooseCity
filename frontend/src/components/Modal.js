import React, { Component } from "react";
import {
  Button,
  Modal,
  ModalHeader,
  ModalBody,
  ModalFooter,
  Form,
  FormGroup,
  Input,
  Label,
} from "reactstrap";

export default class CustomModal extends Component {
  constructor(props) {
    super(props);
    this.state = {
      activeItem: this.props.activeItem,
    };
  }

  handleChange = (e) => {
    let { name, value } = e.target;

    if (e.target.type === "checkbox") {
      value = e.target.checked;
    }

    const activeItem = { ...this.state.activeItem, [name]: value };

    this.setState({ activeItem });
  };

  render() {
    const { toggle, onSave } = this.props;

    return (
      <Modal isOpen={true} toggle={toggle}>
        <ModalHeader toggle={toggle}>Web bb bb</ModalHeader>
        <ModalBody>
          <Form>
            <FormGroup>
              <Label for="product-title">Username</Label>
              <Input
                type="text"
                id="product-title"
                name="product"
                value={this.state.activeItem.title}
                onChange={this.handleChange}
                placeholder="Enter Username"
              />
            </FormGroup>
            <FormGroup>
              <Label for="product-description">Password</Label>
              <Input
                type="text"
                id="product-description"
                name="description"
                value={this.state.activeItem.description}
                onChange={this.handleChange}
                placeholder="Enter Password"
              />
            </FormGroup>
          </Form>
        </ModalBody>
        <ModalFooter>
          <Button
            color="success"
            onClick={() => onSave(window.location.reload())}
          >
            Log in
          </Button>
        </ModalFooter>
      </Modal>
    );
  }
}
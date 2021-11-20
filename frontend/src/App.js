import React, { Component, useState } from "react";
import ProductCard from "./views/general/productCard";
import TableToolbar from "./views/header/header";
import ControlledCarousel from "./views/general/controlled"

class App extends Component {

  // constructor(props) {
  //   super(props);
  //   this.state = {
  //     disable: false,
  //     viewCompleted: true,
  //     todoList: [],
  //     modal: false,
  //     activeItem: {
  //       product_name: "",
  //       description: "",
  //       link: "",
  //       image: "",
  //       condition: "",
  //       prices: 0,
  //       free_returns: true,
  //     },
  //   };
  // }


  render() {
    return (
      <main className="container">
        <ControlledCarousel />
        <h1 className="text-white text-uppercase text-center my-4">app</h1>
        <div className="row">
          <div className="col-md-12 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                {/*<button*/}
                {/*  className="btn btn-primary"*/}
                {/*  onClick={this.createItem}*/}
                {/*>*/}
                {/*  Login*/}
                {/*</button>{'   '}*/}
                {/*<button*/}
                {/*  className="btn btn-primary"*/}
                {/*  onClick={this.createItem}*/}
                {/*>*/}
                {/*  register*/}
                {/*</button>*/}
              </div>
              <ProductCard> </ProductCard>
            </div>
          </div>
        </div>
        {/*{this.state.modal ? (*/}
        {/*  <Modal*/}
        {/*    activeItem={this.state.activeItem}*/}
        {/*    toggle={this.toggle}*/}
        {/*    onSave={this.handleSubmit}*/}
        {/*  />*/}
        {/*) : null}*/}
      </main>
    );
  }
}

export default App;
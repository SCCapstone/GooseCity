import React, { Component, useState } from "react";
import ProductCard from "./views/general/productCard";
import TableToolbar from "./views/header/header";
import ControlledCarousel from "./views/general/controlled"

class App extends Component {


  render() {
    return (
      <main className="container">
        <ControlledCarousel />
        <h1 className="text-white text-uppercase text-center my-4">app</h1>
        <div className="row">
          <div className="col-md-12 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
              </div>
              <ProductCard> </ProductCard>
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default App;
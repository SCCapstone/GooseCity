import React, { Component, useState } from "react";
import ProductCard from "./general/productCard";
import TableToolbar from "./header/header";
import ControlledCarousel from "./general/controlled"

class MainView extends Component {

  render() {
    return (
      <main className="container">
        <header>
            {TableToolbar()}
        </header>
        <div className="row">
          <div className="col-md-12 col-sm-10 mx-auto p-0">
              <ControlledCarousel />
            <div className="card p-3">
              <div className="mb-4">
              </div>
              <ProductCard />
            </div>
          </div>
        </div>
      </main>
    );
  }
}

export default MainView;
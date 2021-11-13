import React, { Component, useState } from "react";
import ProductCard from "./general/productCard";
import TableToolbar from "./header/header";
import ControlledCarousel from "./general/controlled"
import FooterPage from "./footer/footer"
import {Link} from "react-router-dom";


class MainView extends Component {

  render() {
    return (
      <main className="container-fluid">
        <header>
            {TableToolbar()}
        </header>
        <div className="col-md-12 col-sm-10 mx-auto p-0">
            <ControlledCarousel />
        </div>
        <div className="row" style={{paddingRight : 200 , paddingLeft : 200}}>
          <div className="col-md-12 col-sm-10 mx-auto p-0" >
            <div className="card p-3" style={{}}>
                <div >
                    <a className="link" href="#/TempView" style={{color : "black"}}>
                        <h2>Top Views</h2>
                    </a>
                </div>
              <ProductCard />
            </div>
          </div>
        </div>
         < FooterPage/>
      </main>
    );
  }
}

export default MainView;
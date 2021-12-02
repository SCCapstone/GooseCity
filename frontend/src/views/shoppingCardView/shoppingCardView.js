import React, { Component } from "react";
import TableToolbar from "../header/header";
import FooterPage from "../footer/footer"
import ShoppingTable from "./shoppingCardTable";

class ShoppingCardView extends Component {

  render() {
    return (
      <main className="container-fluid">
        <TableToolbar/>
        <ShoppingTable/>
        < FooterPage/>
      </main>
    );
  }
}

export default ShoppingCardView;
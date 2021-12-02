import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import {Image, NavDropdown, Table} from "react-bootstrap";
import axios from "axios";
import {Button} from "@material-ui/core";
import FooterPage from "./footer/footer"
import TableToolbar from "./header/header";
import MainView from "./mainView";
import ProductCard from "./general/productCard";


const Products = (props) => {
  const [isLoading, setLoading] = useState(true);
  const [data, setData] = useState();
  useEffect(() => {
        axios.get("http://localhost:8000/api/todos/"+props.match.params.id+"/").then(response => {
            setData(response.data);
            setLoading(false);
        });
    }, []);

    if (isLoading) {
        return <div className="App">Loading...</div>;
    }
    console.log(props);

    const addCart = async e=>{
        e.preventDefault();
        let data = new FormData();
        let token = window.localStorage.token.replace(/^\"|\"$/g,'');
        data.append("token", token);
        data.append("id", props.match.params.id);
        console.log(data);
        axios.post("http://localhost:8000/addcart/",data).then(res => {
            console.log(res);
            if (res.status===200)
                alert("added to cart!");
            else
                alert.error("error!")
        });
    }
        const Purchase = async e=>{
        e.preventDefault();
        let data = new FormData();
        data.append("id", props.match.params.id);
        data.append("token", token);
        data.append("id", props.match.params.id);
        console.log(data);
        axios.post("http://localhost:3000/#/TempView",data).then(res => {
            console.log(res);
            if (res.status===200)
                alert("Purchase! Thank you!");
            else
                alert("error!")
        });
    }

  return (
    <main className="container-fluid">
       
    <header>
        {/*{TableToolbar}*/}
        <TableToolbar/>
    </header>
  
<div>
  <div>
  <Link className="btn btn-primary" to={{
      pathname: "/",
    }}>
      Main page
  </Link>
  </div>
   
   
  <span style={{paddingLeft: 650}}>
      
      
      <Image src={data.image} style={{width:200, hight:200}} rounded />
      
      
    </span>

    <Table striped bordered hover style={{width:300, hight:300}} align="center" >
      <thead type="thead" className="success">
        <th class="bg-info">Price</th>
      </thead>
      <tbody>
        <tr class="warning">
          <td>${data.prices.match(/\d+(.\d+)?/g)[0]} </td>
          </tr>
      </tbody>
    </Table>


    <span style={{paddingLeft: 1000}}> 
    {
        window.localStorage.token === undefined ?
        null : <Button type="button"  class="btn btn-warning" onClick={addCart}> add Cart</Button>
    }
    </span> 
    <span  style={{paddingTop: 100}}>
    {
        window.localStorage.token === undefined ?
        null : <Button type="button" class="btn-primary" onClick={Purchase}> Buy Now!</Button>
    }
  </span> 
    <div  className="row" style={{paddingRight : 800 , paddingLeft : 800}}>
      <a class="btn btn-info" href={data.link}>Ebay Link</a>
      
  </div>

  </div>
  


  <Table striped bordered hover style={{width:1000, hight:1000}} align="center">
    <thead >
       <tr>
        <th> </th>
            <th colSpan="3">Info</th>
      </tr>
    </thead>
    <tbody>
        <tr>
          <td>product name</td>
          <td colSpan="2">{data.product_name}</td>
        </tr>
        <tr>
          <td>description</td>
          <td colSpan="2">{data.description}</td>
        </tr>
        <tr>
          <td>condition</td>
          <td colSpan="2">{data.condition}</td>
        </tr>
          
        
    </tbody>
  </Table>
  < FooterPage/>
</main>


);
};

export default Products;

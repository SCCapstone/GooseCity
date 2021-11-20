import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import {Image, NavDropdown, Table} from "react-bootstrap";
import axios from "axios";
import {Button} from "@material-ui/core";


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
        const rmCart = async e=>{
        e.preventDefault();
        let data = new FormData();
        let token = window.localStorage.token.replace(/^\"|\"$/g,'');
        data.append("token", token);
        data.append("id", props.match.params.id);
        console.log(data);
        axios.post("http://localhost:8000/rmcart/",data).then(res => {
            console.log(res);
            if (res.status===200)
                alert("removed from cart!");
            else
                alert("error!")
        });
    }

  return (
    <div>
      <Link className="btn btn-primary" to={{
          pathname: "/",
        }}>
          Go Back
      </Link>
        {
            window.localStorage.token === undefined ?
            null : <Button onClick={addCart}> add Cart</Button>
        }
        {
            window.localStorage.token === undefined ?
            null : <Button onClick={rmCart}> remove Cart</Button>
        }
      <div className="form-details">
        <div>
          <Image src={data.image} rounded />
        </div>
        <div>
          <a href={data.link}>Ebay Link</a>
        </div>

      </div>
      <Table striped bordered hover>
        <thead>
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
              <tr>
              <td>prices</td>
              <td colSpan="2">{data.prices}</td>
            </tr>
            <tr>
              <td>id</td>
              <td colSpan="2">{props.match.params.id}</td>
            </tr>
        </tbody>
      </Table>
  </div>

  );
};

export default Products;
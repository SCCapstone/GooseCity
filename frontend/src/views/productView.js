import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import {Image, Table} from "react-bootstrap";
import axios from "axios";


const Example = (props) => {
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
  return (
    <div>
      <Link className="btn btn-primary" to={{
          pathname: "/",
        }}>
          Go Back
      </Link>
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

export default Example;
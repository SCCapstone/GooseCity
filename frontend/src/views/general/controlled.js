import Carousel from 'react-bootstrap/Carousel'
import {useState} from "react";

export default function ControlledCarousel() {
  const [index, setIndex] = useState(0);

  const handleSelect = (selectedIndex, e) => {
    setIndex(selectedIndex);
  };

  return (
    <Carousel activeIndex={index} onSelect={handleSelect} style={{paddingRight : 50, paddingLeft : 50}}>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src="https://i.ebayimg.com/thumbs/images/g/NKEAAOSwqwRgtYMY/s-l225.jpg"
          alt="First slide"
          style={{ height : '30rem', width : '25rem'}}
        />
        <Carousel.Caption>
          {/*<h3>First slide label</h3>*/}
          {/*<p>Nulla vitae elit libero, a pharetra augue mollis interdum.</p>*/}
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src="https://i.ebayimg.com/thumbs/images/g/jRcAAOSwEvJfvN0d/s-l225.jpg"
          style={{ height : '30rem', width : '25rem'}}
        />
        <Carousel.Caption>
          {/*<h3>Second slide label</h3>*/}
          {/*<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>*/}
        </Carousel.Caption>
      </Carousel.Item>
      <Carousel.Item>
        <img
          className="d-block w-100"
          src="https://i.ebayimg.com/thumbs/images/g/0jIAAOSwn0NgvjOQ/s-l225.jpg"
          style={{ height : '30rem', width : '25rem'}}
        />

        <Carousel.Caption>
          {/*<h3>Third slide label</h3>*/}
          {/*<p>*/}
          {/*  Praesent commodo cursus magna, vel scelerisque nisl consectetur.*/}
          {/*</p>*/}
        </Carousel.Caption>
      </Carousel.Item>
    </Carousel>
  );
}

// render(<ControlledCarousel />);

// export default ControlledCarousel;
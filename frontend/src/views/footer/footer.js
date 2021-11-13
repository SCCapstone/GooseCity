import React from "react";

const FooterPage = () => {
  return (

<footer class="page-footer font-small unique-color-dark">
  <div class="container-fluid text-center text-md-left mt-5" style={{backgroundColor: "#F0F3F4"}}>
    <div class="row mt-3">
      <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
        <h6 class="text-uppercase font-weight-bold">Company name</h6>
        <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: "60px"}}/>
        <p>Here you can use rows and columns to organize your footer content. Lorem ipsum dolor sit amet,
          consectetur
          adipisicing elit.
        </p>
      </div>
      <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">

        <h6 class="text-uppercase font-weight-bold">Products</h6>
        <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: "60px"}}/>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>MDBootstrap</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>MDWordPress</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>BrandFlow</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>Bootstrap Angular</a>
        </p>

      </div>

      <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4">


        <h6 class="text-uppercase font-weight-bold">Useful links</h6>
        <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: "60px"}}/>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>Your Account</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>Become an Affiliate</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>Shipping Rates</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>Help</a>
        </p>
      </div>
      <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4">


        <h6 class="text-uppercase font-weight-bold">Contact</h6>
        <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: "60px"}}/>
        <p>
          <i class="fas fa-home mr-3"></i> New York, NY 10012, US</p>
        <p>
          <i class="fas fa-envelope mr-3"></i> info@example.com</p>
        <p>
          <i class="fas fa-phone mr-3"></i> + 01 234 567 88</p>
        <p>
          <i class="fas fa-print mr-3"></i> + 01 234 567 89</p>
      </div>
    </div>
  </div>

  <div class="footer-copyright text-center py-3">© 2020 Copyright:
    <a href="https://mdbootstrap.com/" style={{color : "black", textDecoration: "none"}}> MDBootstrap.com</a>
  </div>
</footer>

  );
}

export default FooterPage;
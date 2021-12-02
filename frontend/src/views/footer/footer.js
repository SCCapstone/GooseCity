import React from "react";

const FooterPage = () => {
  return (

<footer class="page-footer font-small unique-color-dark">
  <div class="container-fluid text-center text-md-left mt-5" style={{backgroundColor: "#F0F3F4"}}>
    <div class="row mt-3">
      <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
        <h6 class="text-uppercase font-weight-bold">GooseCity</h6>
        <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: "60px"}}/>
        <p>
            This is CSCE 490 project. GooseCity is a eCommerce web app.
        </p>
      </div>
      <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4">

        <h6 class="text-uppercase font-weight-bold">Author</h6>
        <hr class="deep-purple accent-2 mb-4 mt-0 d-inline-block mx-auto" style={{width: "60px"}}/>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>zzhuo@email.sc.edu</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>cuic@email.sc.edi</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>xren@email.sc.edu</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>jiabei@email.sc.edu</a>
        </p>
        <p>
          <a href="#/TempView" style={{color : "black", textDecoration: "none"}}>weihang@email.sc.edu</a>
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
          <i class="fas fa-home mr-3"></i> SC, 10012, US</p>
        <p>
          <i class="fas fa-envelope mr-3"></i> XXXX@email.sc.edu</p>
        <p>
          <i class="fas fa-phone mr-3"></i> + 00 000 000 00</p>
        <p>
          <i class="fas fa-print mr-3"></i> + 00 000 000 00</p>
      </div>
    </div>
  </div>
</footer>

  );
}

export default FooterPage;
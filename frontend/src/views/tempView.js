import React from "react";
import {Row} from "react-bootstrap";
import TableToolbar from "./header/header";
import FooterPage from "./footer/footer"


function TempView() {

    return (
        <main>
            <TableToolbar/>
            <Row>
                <h2 className="text-center m-auto">
                    oops! this page is not implemented yet!
                </h2>
            </Row>
            <FooterPage/>
        </main>

    );
}

export default TempView;

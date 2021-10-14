import React from 'react';
import {HashRouter, Route, Switch} from 'react-router-dom';
import App from './App';
import Example from "./views/productView";


const BasicRoute = () => (
    <HashRouter>
        <Switch>
            <Route exact path="/" component={App}/>
            <Route exact path="/product/:id" component={Example}/>
        </Switch>
    </HashRouter>
);


export default BasicRoute;
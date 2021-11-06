import React from 'react';
import {HashRouter, Route, Switch} from 'react-router-dom';
import App from './App';
import Products from "./views/productView";


const BasicRoute = () => (
    <HashRouter>
        <Switch>
            <Route exact path="/" component={App}/>
            <Route exact path="/product/:id" component={Products}/>
        </Switch>
    </HashRouter>
);


export default BasicRoute;
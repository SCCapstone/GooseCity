import React from 'react';
import {HashRouter, Route, Switch} from 'react-router-dom';
import mainView from './views/mainView';
import Products from "./views/productView";


const BasicRoute = () => (
    <HashRouter>
        <Switch>
            <Route exact path="/" component={mainView}/>
            <Route exact path="/product/:id" component={Products}/>
        </Switch>
    </HashRouter>
);


export default BasicRoute;
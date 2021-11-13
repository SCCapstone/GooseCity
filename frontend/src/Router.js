import React from 'react';
import {HashRouter, Route, Switch} from 'react-router-dom';
import mainView from './views/mainView';
import Products from "./views/productView";
import TempView from "./views/tempView";

const BasicRoute = () => (
    <HashRouter>
        <Switch>
            <Route exact path="/" component={mainView}/>
            <Route exact path="/product/:id" component={Products}/>
            <Route exact path="/TempView" component={TempView}/>
        </Switch>
    </HashRouter>
);


export default BasicRoute;
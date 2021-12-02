import React from 'react';
import {HashRouter, Route, Switch} from 'react-router-dom';
import mainView from './views/mainView';
import Products from "./views/productView";
import TempView from "./views/tempView";
import LoginView from "./views/loginView";
import RegisterView from "./views/registerView";
import ShoppingCard from "./views/shoppingCardView/shoppingCardView"

const BasicRoute = () => (
    <HashRouter>
        <Switch>
            <Route exact path="/" component={mainView}/>
            <Route exact path="/product/:id" component={Products}/>
            <Route exact path="/TempView" component={TempView}/>
            <Route exact path="/LoginView" component={LoginView}/>
            <Route exact path="/RegisterView" component={RegisterView}/>
            <Route exact path="/shoppingCard" component={ShoppingCard}/>
        </Switch>
    </HashRouter>
);


export default BasicRoute;
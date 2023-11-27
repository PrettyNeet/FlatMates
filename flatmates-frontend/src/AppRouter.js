// AppRouter.js
import React from 'react';
import { BrowserRouter, Route } from 'react-router-dom';
import Registration from './registration';
import Login from './login';

const AppRouter = () => {
  return (
    <BrowserRouter>
      <Route path="/register" component={Registration} />
      <Route path="/login" component={Login} />
    </BrowserRouter>
  );
};

export default AppRouter;

import React from 'react';
import { BrowserRouter, Route, Switch } from 'react-router-dom';
import Main from './routes/Main';
import Demo from './routes/Demo';
import Analytics from './routes/Analytics';

function LidaRouter() {
  return (
    <BrowserRouter>
      <Switch>
        <Route path="/analytics">
          <Analytics />
        </Route>
        <Route path="/demo">
          <Demo />
        </Route>
        <Route path="/">
          <Main />
        </Route>
      </Switch>
    </BrowserRouter>
  );
}

export default LidaRouter;

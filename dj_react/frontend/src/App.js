// import React, { Component, Fragment } from "react";
// import { Link, BrowserRouter as Router, Route } from 'react-router-dom';

// import Index from "./components/Index";
// import Group from "./components/Group";

// class App extends Component {
//   render() {
//     return (
//       <Fragment>
//         <Index />
//       </Fragment>
//     );
//   }
// }

// class App extends Component {
//   render() {
//     return (
//       <Fragment>
//         <Group />
//       </Fragment>
//     );
//   }
// }

// export default App;


import React, { Component } from 'react';
import { BrowserRouter } from 'react-router-dom';
import { Route, Link } from 'react-router-dom';

import Index from "./components/Index";
import Group from "./components/Group";
import './App.css';
import NewUserForm from './components/NewUserForm';
import NewGroupForm from './components/NewGroupForm';

const BaseLayout = () => (
  <div className="container-fluid">
<nav className="navbar navbar-expand-lg navbar-light bg-light">
  <a className="navbar-brand" href="/">Django React </a>
  <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
    <span className="navbar-toggler-icon"></span>
  </button>
  <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
    <div className="navbar-nav">
      <a className="nav-item nav-link" href="/">USERS</a>
      <a className="nav-item nav-link" href="/groups">GROUPS</a>

    </div>
  </div>
</nav>

    <div className="content">
      <Route path="/" exact component={Index} />
      <Route path="/user/:pk"  component={NewUserForm} />
      <Route path="/groups/" exact component={Group} />
      <Route path="/groups/:pk" exact component={NewGroupForm} />

    </div>

  </div>
)

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <BaseLayout/>
      </BrowserRouter>
    );
  }
}


export default App;

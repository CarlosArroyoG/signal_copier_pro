import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';
import Dashboard from './pages/Dashboard';
import UserRegistration from './pages/UserRegistration';
import AdminPanel from './pages/AdminPanel';

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Switch>
          <Route exact path="/" component={Dashboard} />
          <Route path="/register" component={UserRegistration} />
          <Route path="/admin" component={AdminPanel} />
        </Switch>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
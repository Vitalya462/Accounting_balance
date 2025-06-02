/*import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.tsx</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );import Breadcrumbs from './components/Breadcrumb';<Breadcrumbs />
}

export default App;
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import AppNavbar from './components/Navbar';

import MainPage from './pages/MainPage';
import ServicesListPage from './pages/ServicesListPage';
import ServiceDetailPage from './pages/ServiceDetailPage';

const App: React.FC = () => {
  return (
    <Router>
      <AppNavbar />
      <div className="container mt-4">
        
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/services" element={<ServicesListPage />} />
          <Route path="/service/:id" element={<ServiceDetailPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;*/
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainPage from './pages/MainPage';
import ServicesListPage from './pages/ServicesListPage';
import ServiceDetailPage from './pages/ServiceDetailPage';
import AppNavbar from './components/Navbar';

const App: React.FC = () => {
  return (
    <Router>
      <AppNavbar />
      <div className="container mt-4">
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/services" element={<ServicesListPage />} />
          <Route path="/service/:id" element={<ServiceDetailPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
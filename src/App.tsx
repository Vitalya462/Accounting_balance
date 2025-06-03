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

export default App;
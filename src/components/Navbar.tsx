import React from 'react';
import { Navbar as BsNavbar, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const AppNavbar: React.FC = () => {
  return (
    <BsNavbar bg="dark" variant="dark" expand="lg">
      <BsNavbar.Brand as={Link} to="/">Главная</BsNavbar.Brand>
      <Nav className="me-auto">
        <Nav.Link as={Link} to="/services">Услуги</Nav.Link>
      </Nav>
    </BsNavbar>
  );
};

export default AppNavbar;
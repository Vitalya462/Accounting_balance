import { Navbar as BsNavbar, Nav } from 'react-bootstrap';
import { Link } from 'react-router-dom';

const AppNavbar: React.FC = () => {
  return (
    <BsNavbar expand="md" variant="dark" bg="primary">
      <BsNavbar.Brand as={Link} to="/">Главная</BsNavbar.Brand>
      <BsNavbar.Toggle aria-controls="basic-navbar-nav" />
      <BsNavbar.Collapse id="basic-navbar-nav">
        <Nav className="me-auto">
          <Nav.Link as={Link} to="/services">Услуги</Nav.Link>
        </Nav>
      </BsNavbar.Collapse>
    </BsNavbar>
  );
};

export default AppNavbar;
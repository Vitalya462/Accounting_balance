import React from 'react';
import { Container, Button } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

const MainPage: React.FC = () => {
  return (
    <Container className="text-center py-5">
      <div className="p-4 bg-body rounded shadow-sm d-inline-block w-100" style={{ maxWidth: '600px' }}>
        <h1 className="display-5 fw-bold">Добро пожаловать</h1>
        <p className="lead mb-4">Выберите услугу и забронируйте время.</p>

        <LinkContainer to="/services">
          <Button variant="primary" size="lg">
            Перейти к услугам
          </Button>
        </LinkContainer>
      </div>
    </Container>
  );
};

export default MainPage;
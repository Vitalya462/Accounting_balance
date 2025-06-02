
import React from 'react';
import { Container, Button } from 'react-bootstrap';
// Use LinkContainer + import Link from react-router-bootstrap
import { LinkContainer } from 'react-router-bootstrap';

const MainPage: React.FC = () => {
  return (
    <Container className="mt-5 text-center">
      <div className="p-5 mb-4 bg-body rounded-3">
        <h1 className="display-5 fw-bold">Добро пожаловать в сервис бронирования услуг</h1>
        <p className="fs-4">Выберите из списка доступных услуг и забронируйте удобное время.</p>
        
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
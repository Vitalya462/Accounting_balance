import React from 'react';
import { Card, Button } from 'react-bootstrap';
import { LinkContainer } from 'react-router-bootstrap';

interface ServiceCardProps {
  id: number;
  title: string;
  description: string;
  imageUrl?: string;
  price: number;
}

const DEFAULT_IMAGE = 'https://via.placeholder.com/300x200?text=Нет+изображения';

const ServiceCard: React.FC<ServiceCardProps> = ({ id, title, description, imageUrl, price }) => {
  return (
    <Card className="h-100 shadow-sm">
      <Card.Img variant="top" src={imageUrl || DEFAULT_IMAGE} style={{ height: '200px', objectFit: 'cover' }} />
      <Card.Body className="d-flex flex-column">
        <Card.Title>{title}</Card.Title>
        <Card.Text>{description}</Card.Text>
        <Card.Text className="mt-auto fw-bold">Цена: {price} руб.</Card.Text>
        <LinkContainer to={`/service/${id}`}>
          <Button variant="primary">Подробнее</Button>
        </LinkContainer>
      </Card.Body>
    </Card>
  );
};

export default ServiceCard;
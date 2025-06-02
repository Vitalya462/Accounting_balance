import React from 'react';
import { useParams } from 'react-router-dom';
import { Container, Card, Button } from 'react-bootstrap';

interface ServiceDetail {
  id: number;
  title: string;
  description: string;
  price: number;
  date: string;
  imageUrl?: string;
}

const MOCK_SERVICE_DETAILS: { [key: number]: ServiceDetail } = {
  1: {
    id: 1,
    title: 'Массаж',
    description: 'Релакс массаж спины',
    price: 2000,
    date: '2025-04-01',
    imageUrl: ''
  },
  2: {
    id: 2,
    title: 'Спа',
    description: 'Спа-процедуры для лица',
    price: 4500,
    date: '2025-04-05',
    imageUrl: 'https://picsum.photos/id/1018/300/200' 
  }
};

const ServiceDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const serviceId = parseInt(id || '1');
  const service = MOCK_SERVICE_DETAILS[serviceId];

  return (
    <Container className="mt-5">
      <h2>Детали услуги</h2>
      <Card style={{ width: '30rem', margin: 'auto' }}>
        <Card.Img variant="top" src={service?.imageUrl || 'https://via.placeholder.com/300x200'}  />
        <Card.Body>
          <Card.Title>{service?.title}</Card.Title>
          <Card.Text>{service?.description}</Card.Text>
          <Card.Text><strong>Цена:</strong> {service?.price} руб.</Card.Text>
          <Card.Text><strong>Дата:</strong> {service?.date}</Card.Text>
        </Card.Body>
      </Card>
    </Container>
  );
};

export default ServiceDetailPage;
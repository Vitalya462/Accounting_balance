import React, { useState } from 'react';
import {
  Container,
  Row,
  Col,
  Form,
  Button,
} from 'react-bootstrap';
import ServiceCard from '../components/ServiceCard';

import { Link } from 'react-router-dom';

//import service1Image from '../public/images/service1.jpg';
//import service2Image from '../public/images/service2.jpg';



const service2Image = 'https://i.ibb.co/B5kQknD0/service2.jpg';

const service1Image = 'https://i.ibb.co/RGqx7fNg/service1.jpg';


const ServicesListPage: React.FC = () => {
  const [filterName, setFilterName] = useState<string>('');
  const [minPrice, setMinPrice] = useState<number | null>(null);
  const [maxPrice, setMaxPrice] = useState<number | null>(null);

  const services = [
    {
      id: 1,
      name: "Занимая средства",
      minPrice: 5000,
      subtitle: "Фамилия ребенка: Удаленно",
      description: "Сфера деятельности: Бухгалтерский отчет",
      extraLine: "Мы это оговорены",
      backgroundImage: service1Image,
    },
    {
      id: 2,
      name: "Специальная средства",
      minPrice: 25039,
      subtitle: "Фамилия ребенка: Удаленно",
      description: "Сфера деятельности: Бухгалтерский отчет",
      extraLine: "Мы это оговорены",
      backgroundImage: service2Image,
    },
  ];

  // Apply filters
  const filteredServices = services.filter((service) => {
    const matchesName = service.name.toLowerCase().includes(filterName.toLowerCase());
    const matchesMinPrice = minPrice === null || service.minPrice >= minPrice;
    const matchesMaxPrice = maxPrice === null || service.minPrice <= maxPrice;

    return matchesName && matchesMinPrice && matchesMaxPrice;
  });

  // Show reset button only if any filter is applied
  const showResetButton = filterName !== '' || minPrice !== null || maxPrice !== null;

  return (
    <Container className="mt-5">
      <h2 className="mb-4">Список услуг</h2>

      {/* Filters */}
      <Form className="mb-4 p-3 border rounded bg-light">
        <Row className="gy-3 align-items-center">
          <Col xs={12} md={3}>
            <Form.Group controlId="formName">
              <Form.Label>Фильтр по имени</Form.Label>
              <Form.Control
                type="text"
                placeholder="Введите имя..."
                value={filterName}
                onChange={(e) => setFilterName(e.target.value)}
              />
            </Form.Group>
          </Col>
          <Col xs={12} md={2}>
            <Form.Group controlId="formMinPrice">
              <Form.Label>Мин. цена</Form.Label>
              <Form.Control
                type="number"
                placeholder="Минимум"
                value={minPrice ?? ''}
                onChange={(e) =>
                  setMinPrice(e.target.value ? parseInt(e.target.value) : null)
                }
              />
            </Form.Group>
          </Col>
          <Col xs={12} md={2}>
            <Form.Group controlId="formMaxPrice">
              <Form.Label>Макс. цена</Form.Label>
              <Form.Control
                type="number"
                placeholder="Максимум"
                value={maxPrice ?? ''}
                onChange={(e) =>
                  setMaxPrice(e.target.value ? parseInt(e.target.value) : null)
                }
              />
            </Form.Group>
          </Col>
          {/* Conditionally render the reset button */}
          {showResetButton && (
            <Col xs={12} md={1} className="d-flex justify-content-end">
              <Button
                variant="secondary"
                onClick={() => {
                  setFilterName('');
                  setMinPrice(null);
                  setMaxPrice(null);
                }}
                style={{ width: '100%' }}
              >
                Сброс
              </Button>
            </Col>
          )}
        </Row>
      </Form>

      {/* Cards */}
      <Row xs={1} sm={2} md={2} className="g-4">
        {filteredServices.map((service) => (
          <Col key={service.id}>
            <ServiceCard {...service} />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default ServicesListPage;
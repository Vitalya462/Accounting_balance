import React, { useState, useEffect } from 'react';
import { Container, Row, Col, Form, Button } from 'react-bootstrap';
import ServiceCard from '../components/ServiceCard';
import { fetchServices } from '../utils/api';

const ServicesListPage: React.FC = () => {
  const [filters, setFilters] = useState({
    name: '',
    minPrice: 0,
    maxPrice: Infinity,
    fromDate: '',
    toDate: ''
  });

  const [services, setServices] = useState<any[]>([]); // Will be populated by API or fallback

  // Load services from API
  useEffect(() => {
    const loadServices = async () => {
      const data = await fetchServices(
        filters.name,
        filters.minPrice,
        filters.maxPrice,
        filters.fromDate,
        filters.toDate
      );
      setServices(data);
    };

    loadServices();
  }, [filters]);

  return (
    <Container className="mt-5">
      <h2>Список услуг</h2>

      {/* Filters */}
      <Form className="mb-4 p-3 border rounded bg-light">
        <Row>
          <Col md={3}>
            <Form.Group controlId="formName">
              <Form.Label>Фильтр по имени</Form.Label>
              <Form.Control
                type="text"
                value={filters.name}
                onChange={(e) => setFilters({ ...filters, name: e.target.value })}
              />
            </Form.Group>
          </Col>
          <Col md={2}>
            <Form.Group controlId="formMinPrice">
              <Form.Label>Мин. цена</Form.Label>
              <Form.Control
                type="number"
                value={filters.minPrice}
                onChange={(e) => setFilters({ ...filters, minPrice: Number(e.target.value) })}
              />
            </Form.Group>
          </Col>
          <Col md={2}>
            <Form.Group controlId="formMaxPrice">
              <Form.Label>Макс. цена</Form.Label>
              <Form.Control
                type="number"
                value={filters.maxPrice}
                onChange={(e) => setFilters({ ...filters, maxPrice: Number(e.target.value) })}
              />
            </Form.Group>
          </Col>
          <Col md={2}>
            <Form.Group controlId="formFromDate">
              <Form.Label>С даты</Form.Label>
              <Form.Control
                type="date"
                value={filters.fromDate}
                onChange={(e) => setFilters({ ...filters, fromDate: e.target.value })}
              />
            </Form.Group>
          </Col>
          <Col md={2}>
            <Form.Group controlId="formToDate">
              <Form.Label>По дату</Form.Label>
              <Form.Control
                type="date"
                value={filters.toDate}
                onChange={(e) => setFilters({ ...filters, toDate: e.target.value })}
              />
            </Form.Group>
          </Col>
          <Col md={1} className="d-flex align-items-end">
            <Button variant="secondary" onClick={() => setFilters({
              name: '',
              minPrice: 0,
              maxPrice: Infinity,
              fromDate: '',
              toDate: ''
            })}>
              Сброс
            </Button>
          </Col>
        </Row>
      </Form>

      {/* Cards */}
      <Row xs={1} md={3} className="g-4">
        {services.map((service) => (
          <Col key={service.id}>
            <ServiceCard {...service} />
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default ServicesListPage;
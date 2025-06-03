import React from 'react';
import { useParams } from 'react-router-dom';
import { Container, Button } from 'react-bootstrap';

// Define interface
interface ServiceDetail {
  id: number;
  title: string;
  amount: string;
  childName: string;
  activityArea: string;
  footerText: string;
  backgroundImage: string;
}

// Mock data
const MOCK_SERVICE_DETAILS: Record<number, ServiceDetail> = {
  1: {
    id: 1,
    title: "Занимая средства",
    amount: "от 2000/01P",
    childName: "Удаленно",
    activityArea: "Бухгалтерский отчет",
    footerText: "Мы это оговорены",
    backgroundImage: "https://via.placeholder.com/800x500?text=Занимая+средства"
  },
  2: {
    id: 2,
    title: "Специальная средства",
    amount: "от 20000/01P",
    childName: "Удаленно",
    activityArea: "Бухгалтерский отчет",
    footerText: "Мы это оговорены",
    backgroundImage: "https://via.placeholder.com/800x500?text=Специальная+средства"
  }
};

const ServiceDetailPage: React.FC = () => {
  const { id } = useParams<{ id: string }>();
  const serviceId = parseInt(id || '1');
  const service = MOCK_SERVICE_DETAILS[serviceId];

  // Handle missing service gracefully
  if (!service) {
    return (
      <Container className="mt-5 text-center">
        <h2>Услуга не найдена</h2>
        <p>К сожалению, услуга с указанным идентификатором не существует.</p>
        <Button variant="primary" onClick={() => window.history.back()}>
          Назад
        </Button>
      </Container>
    );
  }

  return (
    <Container className="mt-5 text-center">
      <h2>{service.title}</h2>

      {/* Background Image */}
      <div
        style={{
          backgroundImage: `url(${service.backgroundImage})`,
          backgroundSize: 'cover',
          backgroundPosition: 'center',
          height: '400px',
          position: 'relative',
          overflow: 'hidden',
          borderRadius: '8px',
          color: '#fff', 
          display: 'flex',
          alignItems: 'flex-end',
          justifyContent: 'center',
          marginBottom: '30px',
        }}
      >
        <div
          style={{
            padding: '30px',
            backgroundColor: 'rgba(0, 0, 0, 0.6)',
            width: '100%',
            maxWidth: '500px',
            textAlign: 'center',
          }}
        >
          <p><strong>Стоимость:</strong> {service.amount}</p>
          <p><strong>Фамилия ребенка:</strong> {service.childName}</p>
          <p><strong>Сфера деятельности:</strong> {service.activityArea}</p>
          <p>{service.footerText}</p>
        </div>
      </div>

      {/* Back Button */}
      <Button variant="primary" onClick={() => window.history.back()}>
        Назад
      </Button>
    </Container>
  );
};

export default ServiceDetailPage;
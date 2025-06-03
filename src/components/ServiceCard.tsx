import React, { useState, MouseEvent, FormEvent } from 'react';
import { Button } from 'react-bootstrap';
import '../ServiceCard.css';
// No longer importing { Link } from 'react-router-dom';

interface IServiceCardProps {
  id: number;
  name: string;
  minPrice: number;
  subtitle: string;
  description: string;
  extraLine: string;
  backgroundImage: string;
}

const ServiceCard: React.FC<IServiceCardProps> = ({
  id,
  name: serviceName,
  minPrice,
  subtitle,
  description,
  extraLine,
  backgroundImage,
}) => {
  const [showInterestForm, setShowInterestForm] = useState(false);
  const [clientName, setClientName] = useState('');
  const [clientPhone, setClientPhone] = useState('');

  const handleInterestButtonClick = (event: MouseEvent<HTMLElement>) => {
    event.stopPropagation(); // Prevent event from bubbling to parent elements
    setShowInterestForm(true);
  };

  const handleFormSubmit = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault(); // Essential to prevent default form submission (page reload)
    event.stopPropagation();

    if (!clientName.trim() || !clientPhone.trim()) {
      alert('Пожалуйста, заполните имя и телефон.');
      return;
    }

    console.log({
      serviceId: id,
      serviceName,
      clientName,
      clientPhone,
    });
    alert(`Спасибо, ${clientName}! Ваша заявка на услугу "${serviceName}" принята. Мы скоро свяжемся с вами по номеру ${clientPhone}.`);

    setClientName('');
    setClientPhone('');
    setShowInterestForm(false);
  };

  const handleCancelForm = (event: MouseEvent<HTMLElement>) => {
    event.stopPropagation();
    setShowInterestForm(false);
    setClientName('');
    setClientPhone('');
  };

  const handleOverlayClick = (event: MouseEvent<HTMLDivElement>) => {
    // If the form is shown, clicks on the overlay backdrop (not the form itself,
    // which handles its own stopPropagation) should also stop propagation.
    // You could also choose to close the form here if desired (e.g., setShowInterestForm(false)).
    if (showInterestForm) {
      event.stopPropagation();
    }
  }

  return (
    // Replaced Link with a div. Kept className for styling consistency.
    <div
      className="service-card-link" // Assuming this class styles the card container
    >
      <div
        className="service-card"
        style={{ backgroundImage: `url(${backgroundImage})` }}
        // The aria-hidden="true" was on this div. Consider its implications
        // now that the parent is not an interactive Link.
        // Content within the card (text, form) should remain accessible.
        aria-hidden="true"
      >
        <div className="service-card-title">
          <h3>{serviceName}</h3>
          <p>от {minPrice.toLocaleString()} ₽</p>
        </div>

        <div className="service-card-overlay" onClick={handleOverlayClick}>
          {showInterestForm ? (
            <form className="interest-form" onSubmit={handleFormSubmit} onClick={(e) => e.stopPropagation()}>
              <h4>Заинтересовала услуга?</h4>
              <p>Оставьте ваши контакты, и мы свяжемся с вами.</p>
              <div className="form-group">
                <label htmlFor={`form-name-${id}`}>Имя:</label>
                <input
                  type="text"
                  id={`form-name-${id}`}
                  value={clientName}
                  onChange={(e) => setClientName(e.target.value)}
                  onClick={(e) => e.stopPropagation()}
                  required
                  aria-required="true"
                />
              </div>
              <div className="form-group">
                <label htmlFor={`form-phone-${id}`}>Телефон:</label>
                <input
                  type="tel"
                  id={`form-phone-${id}`}
                  value={clientPhone}
                  onChange={(e) => setClientPhone(e.target.value)}
                  onClick={(e) => e.stopPropagation()}
                  required
                  aria-required="true"
                />
              </div>
              <div className="interest-form-buttons">
                <Button type="submit" className="submit-interest-button">
                  Отправить
                </Button>
                <Button
                  type="button"
                  variant="secondary"
                  onClick={handleCancelForm}
                  className="cancel-interest-button"
                >
                  Отмена
                </Button>
              </div>
            </form>
          ) : (
            <>
              <p>{subtitle}</p>
              <p>{description}</p>
              <p>{extraLine}</p>
              <div className="service-card-buttons">
                <Button
                  className="interest-button"
                  onClick={handleInterestButtonClick}
                >
                  Мне это интересно
                </Button>
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
};

export default ServiceCard;
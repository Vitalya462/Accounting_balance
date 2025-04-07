FROM python:3.13

ENV POETRY_VERSION=1.7.1 
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="/root/.local/bin:$PATH"

WORKDIR /app

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && poetry install --no-dev --no-interaction --no-ansi

COPY . .

RUN python manage.py migrate && python manage.py collectstatic --noinput

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
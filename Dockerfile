FROM python:3.13

COPY backend /app
WORKDIR /app
EXPOSE 8000

COPY requirements.txt /temp/requirements.txt

RUN pip install -r /temp/requirements.txt
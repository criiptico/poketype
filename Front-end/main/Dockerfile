FROM python:3.10.12

RUN pip install Flask pydantic requests gunicorn PokeTypeAdvantage

COPY ../../Front-end app/
WORKDIR /app

ENV PORT 8080

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app

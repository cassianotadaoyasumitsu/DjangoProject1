ARG PYTHON_VERSION=3.9-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN apt-get update && apt-get install -y gcc build-essential && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/

COPY . /code

EXPOSE 8000

CMD ["gunicorn","--bind",":8000","--workers","2","django_test.wsgi"]

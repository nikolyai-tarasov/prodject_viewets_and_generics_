FROM python:3.12.4-slim

WORKDIR /app

RUN apt-get update \
    && apt-get install -y gcc libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


# ENV SECRET_KEY="django-insecure-f&nyor#v!!#luf4&)8$nj@(s5lsq2%+$ejb5m9euvim3*_w@)9"
# ENV CELERY_BROKER_URL="redis://localhost:6379/0"
# ENV CELERY_BACKEND="redis://localhost:6379/0"

RUN mkdir -p /app/media

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
FROM python:3.9-slim


ENV PYTHONDONTWRITEBYCODE=1
ENV PYTHONBUFFERED=1

RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean
WORKDIR /app
COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt
COPY  . /app/

RUN chmod +x /app/entrypoint.sh

EXPOSE 8000

ENTRYPOINT [ "/app/entrypoint.sh" ]
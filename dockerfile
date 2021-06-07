FROM python:3.8.5-alpine
WORKDIR /app
COPY ./myproj /app
COPY ./requirement.txt /app
RUN  apk add build-base && apk add postgresql-dev  && pip install --upgrade pip  && pip install -r requirement.txt && pip install psycopg2
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
COPY ./entry.sh /app
CMD ["sh", "entry.sh"]

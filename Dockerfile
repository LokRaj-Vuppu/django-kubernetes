FROM python:3.12-alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN apk update && \
    apk add --no-cache \
    build-base \
    postgresql-dev \
    gettext


# create a directory app in docker and copy app folder contents from local machine to container
RUN mkdir /app
COPY ./app /app
WORKDIR /app
COPY ./requirements.txt .

# creating and activating virtualenv
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"


RUN pip install --upgrade pip && pip install -r requirements.txt

# creating static and media files directories
RUN mkdir -p /vol/shared/static /vol/shared/media /staticfiles
# RUN adduser -D appuser
# RUN chown -R appuser:appuser /vol/shared /staticfiles
# RUN chmod -R 755 /vol/shared

# USER appuser

EXPOSE 8000
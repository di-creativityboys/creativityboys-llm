FROM python:3.11-bullseye

WORKDIR /app

ENV PYTHONUNBUFFERED 1

ENV WS_HOST=0.0.0.0
ENV WS_PORT=5000

COPY requirements.txt /tmp/pip-tmp/
RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
    && rm -rf /tmp/pip-tmp

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive 

COPY . .

EXPOSE 5000

CMD ["python3", "src/main.py"]
FROM python:3.9-slim

RUN useradd -rm -d /home/student -s /bin/bash -u 1001 student

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir --upgrade -r requirements.txt && \
    rm /requirements.txt

COPY data /data
RUN chmod a=rx /data && chmod a=r /data/*

WORKDIR /agent
COPY launch.py utils.py /agent/
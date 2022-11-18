FROM python:latest

RUN apt update \
    && apt install -y python3-pip \
    && pip install sklearn \
    && pip install boto3 \
    && rm -rf /var/lib/apt/lists/*

COPY train.py .

ENTRYPOINT [ "python", "train.py"]
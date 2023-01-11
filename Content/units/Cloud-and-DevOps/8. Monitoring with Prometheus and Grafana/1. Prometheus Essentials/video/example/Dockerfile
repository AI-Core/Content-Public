FROM python:latest

COPY example.py example.py

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "example.py"]
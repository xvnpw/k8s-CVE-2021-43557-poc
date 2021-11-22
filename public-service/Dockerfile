FROM python:3

RUN apt-get update -y && \
    apt-get install -y curl tcpdump

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY app.py app.py

CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0"]
FROM python:3.8-slim-buster

RUN pip install --upgrade pip

WORKDIR /app

RUN pip install -U Flask

COPY . .
EXPOSE 5000
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

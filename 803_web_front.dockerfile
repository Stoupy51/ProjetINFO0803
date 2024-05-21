
# Build command: docker build -t 803_web__front.dockerfile .

FROM python:latest

WORKDIR /app
COPY ./code_web_front /app
RUN pip install -r requirements.txt

EXPOSE 80


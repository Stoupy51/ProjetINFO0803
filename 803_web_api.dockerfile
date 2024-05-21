
# Build command: docker build -t 803_web_api.dockerfile .

FROM python:latest

WORKDIR /app
COPY ./code_web_api /app
RUN pip install -r requirements.txt

EXPOSE 5000


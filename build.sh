
docker build -t 803_database --file 803_database.dockerfile .
docker build -t 803_web_api --file 803_web_api.dockerfile .
docker build -t 803_web_front --file 803_web_front.dockerfile .
docker compose up


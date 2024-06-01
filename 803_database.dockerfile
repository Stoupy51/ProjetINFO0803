
# Build command: docker build -t 803_database --file 803_database.dockerfile .

FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=projet_803_password
ENV MYSQL_USER=projet_803
ENV MYSQL_PASSWORD=projet_803_password

# Setup database data
ADD ./data/init.sql /docker-entrypoint-initdb.d

EXPOSE 3306


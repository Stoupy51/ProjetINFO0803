# Build command: docker build -t 803_database --file 803_database.dockerfile .

FROM mysql:latest

ENV MYSQL_ROOT_PASSWORD=projet_803_password
ENV MYSQL_DATABASE=projet_803
ENV MYSQL_USER=projet_803
ENV MYSQL_PASSWORD=projet_803_password

# Setup database data
#COPY init.sql /803_database/data/init.sql
ADD ./data/init.sql /docker-entrypoint-initdb.d
#RUN mysql -u root -p$MYSQL_ROOT_PASSWORD < /803_database/data/init.sql

EXPOSE 3306


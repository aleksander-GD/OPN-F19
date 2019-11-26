FROM mysql

ENV MYSQL_ALLOW_EMPTY_PASSWORD yes

COPY initDB/init.sql /docker-entrypoint-initdb.d/

FROM mysql:5.7 as BASE

LABEL maintainer="http://github.com/thiagolsfortunato"

ADD create_database.sql /docker-entrypoint-initdb.d/

ENV MYSQL_ROOT_PASSWORD datadog
ENV MYSQL_DATABASE chat
ENV MYSQL_USER datadog
ENV MYSQL_PASSWORD datadog

EXPOSE 3306

FROM python:3.6-slim-stretch as base

LABEL maintainer="http://github.com/thiagolsfortunato"

WORKDIR /app

FROM base as build

COPY requirements.txt ./

RUN pip install -r requirements.txt

FROM base as release

COPY --from=build /usr/local /usr/local
COPY src/app.py ./

EXPOSE 8001

CMD ddtrace-run python app.py

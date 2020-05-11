FROM python:3.6-alpine as base

LABEL maintainer="http://github.com/thiagolsfortunato"

WORKDIR /app

FROM base as build

COPY requirements.txt ./

RUN pip install -r requirements.txt

FROM base as release

COPY --from=build /usr/local /usr/local
COPY app.py ./

CMD python app.py
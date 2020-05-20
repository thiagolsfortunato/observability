FROM node:12-alpine as base

LABEL maintainer="http://github.com/thiagolsfortunato"

WORKDIR /app

FROM base as build

COPY package.json package-lock.json ./

RUN npm install

FROM base as release

COPY --from=build /app/node_modules /app/node_modules 
COPY . ./

EXPOSE 3000

CMD node /app/bin/message
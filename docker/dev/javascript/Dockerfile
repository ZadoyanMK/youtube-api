FROM node:10.16-alpine

COPY ./package.json /src_frontend/package.json

WORKDIR /src_frontend

RUN npm install --quiet

COPY ./src_frontend .
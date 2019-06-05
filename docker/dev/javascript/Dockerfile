FROM node:10.16-alpine

COPY ./src_frontend/package.json /src_frontend/package.json

WORKDIR /src_frontend

RUN npm install --quiet

COPY ./src_frontend .
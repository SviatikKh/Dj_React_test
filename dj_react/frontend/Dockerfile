FROM node:14.15.1-alpine3.10

# set work directory
WORKDIR /app

ENV PATH /app/node_modules/.bin:$PATH

COPY package.json /app/package.json
RUN npm install

# copy project
COPY . /app

CMD npm start
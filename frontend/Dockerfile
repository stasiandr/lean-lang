FROM node:16-alpine
# vue-cli reqires 8.10.0+ 

# RUN apt-get -y update

RUN npm install -g @vue/cli

WORKDIR /code

EXPOSE 8080

USER node

CMD ["npm", "run", "serve"]
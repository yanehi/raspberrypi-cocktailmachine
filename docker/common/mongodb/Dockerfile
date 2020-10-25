FROM alpine:edge

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories \
	&& echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories \
	&& apk update \
	&& apk add mongodb=3.4.4-r0

EXPOSE 27017 27017

VOLUME /data/db

CMD [ "mongod" ]
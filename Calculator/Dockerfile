FROM alpine:latest

# basic flask environment
# Added for docx python3-dev libc-dev libxml2-dev libxslt-dev jpeg jpeg-dev libjpeg zlib zlib-dev gcc
RUN apk --no-cache update \
	&& apk add --no-cache ca-certificates bash curl python3 py3-pip nginx uwsgi uwsgi-python3 libc6-compat python3-dev libc-dev libxml2-dev libxslt-dev jpeg jpeg-dev libjpeg zlib zlib-dev gcc\
	&& rm -rf /var/cache/apk/* \
	&& pip3 install --upgrade pip \
	&& pip3 install flask requests flask-wtf wtforms python-docx docx2pdf werkzeug
	# && mkdir xray-daemon && cd xray-daemon \
	# && curl https://s3.dualstack.ap-southeast-2.amazonaws.com/aws-xray-assets.ap-southeast-2/xray-daemon/aws-xray-daemon-linux-2.x.zip -o ./aws-xray-daemon-linux-2.x.zip \
	# && unzip -o aws-xray-daemon-linux-2.x.zip -d . \
	# && cp xray /usr/local/bin/xray-daemon \
	# && chmod 744 /usr/local/bin/xray-daemon

# application folder
ENV APP_DIR /app
ARG REGION=ap-southeast-2
ENV AWS_DEFAULT_REGION=${REGION}

# app dir
RUN mkdir ${APP_DIR}
VOLUME [${APP_DIR}]
WORKDIR ${APP_DIR}

# Copy flask app to /app
COPY flask /app
RUN chown -R nginx:nginx ${APP_DIR} \
	&& chmod 777 /run/ -R \
	&& chmod 777 /root/ -R

# expose web server port
# only http, for ssl use reverse proxy
EXPOSE 80

# copy config files into filesystem
COPY nginx.conf /etc/nginx/nginx.conf
COPY app.ini /app.ini
COPY entrypoint.sh /entrypoint.sh

# exectute start up script
ENTRYPOINT ["/entrypoint.sh"]

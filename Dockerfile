FROM farseer810/ubuntu:16.04

WORKDIR /var/www/html

RUN apt-get update && \
apt-get install -y software-properties-common python-software-properties

RUN apt-get install -y php7.0-curl php7.0-dev php7.0-gd php7.0-imap php7.0-intl \
php7.0-mbstring php7.0-mysql php7.0-xml php7.0-zip php7.0-fpm

RUN apt-get install -y nginx && \
rm -f /var/www/html/index.html /var/www/html/index.nginx-debian.html && \
rm -f /var/www/html/index.hml && \
chmod 777 /var/www/html && \
mkdir /run/php

ADD . /var/www/html

RUN rm /etc/nginx/sites-enabled/default && \
cat /var/www/html/nginx-site > /etc/nginx/sites-enabled/nginx-site && \
rm -f Dockerfile nginx-site && \
chmod -f -R 777 /var/www/html

EXPOSE 80

CMD python3 setup.py && rm -f setup.py && php-fpm7.0 && nginx -g "daemon off;"
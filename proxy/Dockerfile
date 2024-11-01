FROM nginxinc/nginx-unprivileged:1.26-alpine

COPY ./default.conf /etc/nginx/conf.d/default.conf

USER root

RUN mkdir -p /vol/shared /var/logs/nginx /mnt/data/logs
RUN chmod 755 /vol/shared /var/logs/nginx /mnt/data/logs

USER nginx
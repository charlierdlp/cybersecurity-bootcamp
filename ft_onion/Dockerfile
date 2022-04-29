FROM debian:buster

RUN apt-get update && apt-get install -y \
	nginx tor openssh-server

COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY ./conf/torrc /etc/tor
COPY ./conf/index.html /var/www/index.html
COPY ./conf/sshd_config /etc/ssh/sshd_config

#sustituir proceso principal por nginx
#CMD ["nginx", "-g", "daemon off;"]
#CMD ["tor", "-f", "/etc/tor/torrc"]

RUN useradd ssh_user \
        && echo "ssh_user:secret" | chpasswd \
        && mkdir /home/ssh_user \
        && chown ssh_user:ssh_user /home/ssh_user

#RUN service ssh start
ENTRYPOINT nginx ; tor

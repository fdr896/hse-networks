FROM ubuntu:latest

WORKDIR /app
COPY ./find_mtu.py /app/find_mtu

RUN apt-get update --yes
RUN apt-get install iputils-ping --yes
RUN apt-get install python3 --yes

RUN chmod +x /app/find_mtu
ENTRYPOINT ["/app/find_mtu"]

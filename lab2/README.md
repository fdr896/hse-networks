## Описание решения

Данная консольная утилита позволяет найти минимальный MTU на пути между локальный хостом и указанным удалённым.

#### Сборка docker-образа и запуск

```bash
$ sudo docker build . -t find_mtu -f Dockerfile
Sending build context to Docker daemon   5.12kB
Step 1/8 : FROM ubuntu:latest
 ---> a8780b506fa4
Step 2/8 : WORKDIR /app
 ---> Using cache
 ---> ec4a0bd2ed75
Step 3/8 : COPY ./find_mtu.py /app/find_mtu
 ---> Using cache
 ---> 035f76022a29
Step 4/8 : RUN apt-get update --yes
 ---> Using cache
 ---> ffb07ff07425
Step 5/8 : RUN apt-get install iputils-ping --yes
 ---> Using cache
 ---> a87d1dc280fb
Step 6/8 : RUN apt-get install python3 --yes
 ---> Using cache
 ---> 926a23e0c638
Step 7/8 : RUN chmod +x /app/find_mtu
 ---> Using cache
 ---> 5db3b096ce9e
Step 8/8 : ENTRYPOINT ["/app/find_mtu"]
 ---> Running in e4f795c532b4
Removing intermediate container e4f795c532b4
 ---> ad32079bffcc
Successfully built ad32079bffcc
Successfully tagged find_mtu:latest
$ sudo docker run --rm find_mtu --dest ya.ru

------------[FIND MINUM MTU BETWEEN YOUR HOST AND ya.ru]------------

------------[CHECK IF CONNECTION EXISTS]------------

------------[SUCCESS]------------

------------[FINDING MTU UPPER BOUND]------------

------------[MTU IS AT LEAST: 30]------------

------------[MTU IS AT LEAST: 32]------------

------------[MTU IS AT LEAST: 36]------------

------------[MTU IS AT LEAST: 44]------------

------------[MTU IS AT LEAST: 60]------------

------------[MTU IS AT LEAST: 92]------------

------------[MTU IS AT LEAST: 156]------------

------------[MTU IS AT LEAST: 284]------------

------------[MTU IS AT LEAST: 540]------------

------------[MTU IS AT LEAST: 1052]------------

------------[MTU IS AT LEAST: 2076]------------

------------[FINDING MINUM MTU]------------

------------[MTU LOWER THAN 2076]------------

------------[MTU AT LEAST 1052]------------

------------[MTU LOWER THAN 1564]------------

------------[MTU AT LEAST 1308]------------

------------[MTU AT LEAST 1436]------------

------------[MTU AT LEAST 1500]------------

------------[MTU LOWER THAN 1532]------------

------------[MTU LOWER THAN 1516]------------

------------[MTU LOWER THAN 1508]------------

------------[MTU LOWER THAN 1504]------------

------------[MTU LOWER THAN 1502]------------

------------[MTU LOWER THAN 1501]------------

------------[MINUMUM MTU BETWEEN YOUR HOST AND ya.ru IS 1500]------------
```

#### Обработка некорректных и недостижимых хостов
```bash
$ sudo docker run --rm find_mtu --dest yaaaa.ru

------------[FIND MINUM MTU BETWEEN YOUR HOST AND yaaaa.ru]------------

------------[CHECK IF CONNECTION EXISTS]------------

------------[CONNECTION IS UNAVAILABLE BECAUSE ERROR OCCURED:
 ping: yaaaa.ru: Name or service not known
]------------
$ sudo docker run --rm find_mtu --dest www.maladidaho.org

------------[FIND MINUM MTU BETWEEN YOUR HOST AND www.maladidaho.org]------------

------------[CHECK IF CONNECTION EXISTS]------------

------------[CONNECTION IS UNAVAILABLE BECAUSE ERROR OCCURED:
 PING www.maladidaho.org (199.34.228.57) 0(28) bytes of data.

--- www.maladidaho.org ping statistics ---
1 packets transmitted, 0 received, 100% packet loss, time 0ms

]------------
$
```
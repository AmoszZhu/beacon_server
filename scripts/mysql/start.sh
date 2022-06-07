#! /bin/bash

if [ "$1" = "start" ]; then
  docker run -d -p 3306:3306 --privileged=true -v ~/code/beacon_server/scripts/mysql/mysql-master.cnf:/etc/mysql/my.cnf -e MYSQL_ROOT_PASSWORD=zj122900 --name mysql-master mysql:5.7
  docker run -d -p 3307:3307 --privileged=true -v ~/code/beacon_server/scripts/mysql/mysql-slave.cnf:/etc/mysql/my.cnf -e MYSQL_ROOT_PASSWORD=zj122900 --name mysql-slave mysql:5.7
fi

if [ "$1" = "stop" ]; then
  docker stop mysql-master
  docker rm mysql-master
  docker stop mysql-slave
  docker rm mysql-slave
fi

exit 0

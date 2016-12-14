#!/bin/bash

cat << EOF|mysql -u root -p -v
create user 'flask'@'localhost' identified by '123456';
create database flask default character set=utf8;
grant all on flask.* to 'flask'@'localhost';
EOF


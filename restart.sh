#!/bin/sh
ps aux|grep walry.ini|grep -v grep|cut -c 9-15|xargs kill -s 9
setsid nohup uwsgi walry.ini &

#! /bin/sh
sudo /usr/local/bin/forever start -c "npm start --prefix=/home/pi/foosball" /home/pi/foosball > /var/log/foosball.log

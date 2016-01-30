/etc/init.d/theo-startup
sudo crontab -l

sudo /etc/init.d/theo-startup stop
/home/pi/theo/test/node_modules/mqtt/bin/


//potwierdzenie, ze dziala po WS:

mqtt sub -t 'pirTopic' -h 'localhost' -v -l 'ws' -p 9001

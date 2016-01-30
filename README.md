# foosball-backend

* install Python >= 2.7.3
* install mosquitto >= version 1.4.7
* npm install forever -g

* copy etc/init.d/theo-startup to /etc/init.d/
* check path to mosquitto.conf at theo-startup
* chmod /755 etc/init.d/theo-startup
* run update-rc.d theo-startup defaults
* check /etc/init.d/theo-startup start/stop

* download https://github.com/DexterInd/GrovePi

* sudo crontab -e
* add to crontab : 
@reboot /home/pi/theo/cron-startup.sh
@reboot /home/pi/theo/cron-startup-npm.sh

* check websocket connection via mqtt sub -t 'pirTopic' -h 'localhost' -v -l 'ws' -p 9001

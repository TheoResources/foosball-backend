import paho.mqtt.client as mqtt
import time
import grovepi
from datetime import datetime, timedelta

pir_sensor = 8
grovepi.pinMode(pir_sensor,"INPUT")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.loop_start()
lastDtime = datetime(1000, 1, 1)

while True:
    try:
        # Sense motion, usually human, within the target range
        if grovepi.digitalRead(pir_sensor):
            print 'Motion Detected'
	    client.publish("pirTopic", "Motion Detected")
	    lastDtime = datetime.now()
	else:
            now = datetime.now()
            xSec = now - timedelta(seconds=10)
            if lastDtime > xSec:
	        print 'Motion Detected'
	    	client.publish("pirTopic", "Motion Detected")
            else:
	    	print '-'
            	client.publish("pirTopic", "-")

        # if your hold time is less than this, you might not see as many detections
        time.sleep(.2)

    except IOError:
        client.publish("pirTopic", "Motion Detected")
        print "Error"

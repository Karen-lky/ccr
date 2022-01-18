import paho.mqtt.client as mqtt
from jsonmerge import merge
import numpy as np
import json
import time


sensor_count = 4


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe("rwth/cr/PP/CCR/Attachment1")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


#MQTT Settings
client = mqtt.Client("CCR_test")
client.on_connect = on_connect
client.on_message = on_message
client.connect('broker.mqttdashboard.com', 1883, 17300)




while True:

    for a in range (10):
        for i in range(sensor_count):
            sensor = "Sensor%s" % str(i + 1)
            angle = a*18
            distance = np.random.randint(1000)

            globals()['JSON%s' % str(i + 1)] = {}
            globals()['JSON%s' % str(i + 1)][sensor] = angle , distance


        part1 = merge(JSON1,JSON2)
        part2 = merge(JSON3,JSON4)


        Payload = merge(part1, part2)

        payload = json.dumps(Payload)

        print(payload)

        client.publish("rwth/cr/PP/CCR/Attachment1", payload )


        time.sleep(.5)


client.loop_forever()
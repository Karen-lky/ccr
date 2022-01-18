# incoming data example in JSON format: {"Sensor1":[80,100],"Sensor2":[80,100],"Sensor3":[90,100],"Sensor4":[90,100]}

import paho.mqtt.client as mqtt  # http://www.hivemq.com/demos/websocket-client/
import matplotlib.pyplot as plt
import numpy as np
import json

sensor_count = 4  # Set the number of sensors (works for single half for now)
sensor_position_offset = 26  # Set angle offset between the sensors on attachment


def on_connect(client, userdata, flags, rc):
    print("Connected with result code {0}".format(str(rc)))
    client.subscribe("rwth/cr/PP/CCR/Attachment1")


def rotate(p, origin=(0, 0), degrees=0):  # rotate on 2D plane
    angle = np.deg2rad(degrees)
    R = np.array([[np.cos(angle), -np.sin(angle)],
                  [np.sin(angle), np.cos(angle)]])
    o = np.atleast_2d(origin)
    p = np.atleast_2d(p)
    return np.squeeze((R @ (p.T - o.T) + o.T).T)


def pol2cart(rho, phi):  # Polar Coordinates to point conversion
    x = rho * np.cos(phi)
    y = rho * np.sin(phi)
    return x, y


fig = plt.figure()
ax = fig.add_subplot(projection='3d')

ax.set_xlim3d(-400, 400)
ax.set_ylim3d(-400, 400)
ax.set_zlim3d(-400, 400)

ax.scatter(0, 0, 0,s=90, c='k', marker='h') # Mark Origin for Attachment

colors = ['brown', 'red', 'orange', 'gold', 'yellow', 'lawngreen', 'aquamarine', 'deepskyblue', 'navy', 'b', 'darkviolet', 'magenta']

for i in range(sensor_count):  # Initialize lists based on the sensor count
    globals()['angle%s' % str(i + 1)] = []
    globals()['distance%s' % str(i + 1)] = []
    globals()['point%s' % str(i + 1)] = []


def save_MQTTdata(payload):  # Saves Data coming through MQTT, sets lists to empty when angle 0 or 180 is reached

    msg = str(payload)
    msg = msg[2:-1:]  # Remove unnecessary letters from received payload
    msg = json.loads(msg)

    for i in range(sensor_count):  # Append list for each sensor data

        if msg['Sensor%s' % str(i + 1)][0] not in globals()['angle%s' % str(i + 1)]:  # Check for unique angle data
            globals()['angle%s' % str(i + 1)].append(msg['Sensor%s' % str(i + 1)][0])
            globals()['distance%s' % str(i + 1)].append(msg['Sensor%s' % str(i + 1)][1])

        if 0 in globals()['angle%s' % str(i + 1)] or 20 in globals()['angle%s' % str(i + 1)]:  # Set list to empty if 0 or 180 reached
            globals()['angle%s' % str(i + 1)] = []
            globals()['distance%s' % str(i + 1)] = []


def get_Points():
    for i in range(sensor_count):

        for s in range(len(globals()['distance%s' % str(i + 1)])):

            x_base = np.sin(np.radians(globals()['angle%s' % str(i + 1)][s])) * globals()['distance%s' % str(i + 1)][s]
            y_base = 0

            rotated_xy = rotate((x_base, y_base), origin=(0, 0), degrees=((90 + (sensor_position_offset * 1.5)) - sensor_position_offset * i))

            x = rotated_xy[0]
            y = rotated_xy[1]

            z = np.cos(np.radians(globals()['angle%s' % str(i + 1)][s])) * globals()['distance%s' % str(i + 1)][s]

            coordinates = [x, y, -z]

            if coordinates not in globals()['point%s' % str(i + 1)]:  # Check for unique coordinate data
                globals()['point%s' % str(i + 1)].append(coordinates)

            if len(globals()['distance%s' % str(i + 1)]) <= 1:  # Empty list when 0 or 180
                globals()['point%s' % str(i + 1)] = []

            if len(globals()['point%s' % str(i + 1)]) > 0:  # Plot points list --> Work in Progress
                ax.scatter(globals()['point%s' % str(i + 1)][s][0], globals()['point%s' % str(i + 1)][s][1],
                           globals()['point%s' % str(i + 1)][s][2], c=colors[i], marker='o')


def on_message(client, userdata, msg):
    save_MQTTdata(msg.payload)

    get_Points()

    if len(point1) > 0: # Preview data on demand

        # print(distance1)
        # print(distance2)

        # print(angle1)
        # print(angle2)

        print(point1)
        # print(point2)

    if len(point1) >= 3:  # Work in progress, right now only prints when certain points are recorded for real-time plotting

        plt.show()


client = mqtt.Client("CCR_test")
client.on_connect = on_connect
client.on_message = on_message

client.connect('broker.mqttdashboard.com', 1883, 17300)
client.loop_forever()

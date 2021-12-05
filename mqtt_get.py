#control only send out one angel per distance - prevent overflow of data, maybe is better
#only store 1 data get angle, (unqiue)
#once 180 degree empty data reset!!!

#mqtt connection
from os import write
import paho.mqtt.client as mqtt
import pandas as pd
import csv
import numpy

server = "broker.hivemq.com"
topic = "rwth/cr/PP/CCR/#"
received_messages=[] #define empty list to store msg
#store msg in different table for plotting later
S1 = [] #create empty list to store
S2 = []
S3 = []
S4 = []
S5 = []
S6 = []
S7 = []
S8 = []
S9 = []
S10 = []
subList = []
k = len(subList)-1
cmpre_list = ['0','180']
angle1 = []
angle2 = []
angle3 = []
angle4 = []
angle5 = []
angle6 = []
angle7 = []
angle8 = []
angle9 = []
angle10 = []


#clear all old sensor data
for no in range(1,10):    
    fileVariable = open('S'+ str(no) +'.csv',"r+")
    fileVariable.truncate(0)
    fileVariable.close()

def on_connect(client, userdata, flags, rc):  # The callback for when the client connects to the broker
    print("Connected with result code {0}".format(str(rc)))  # Print result of connection attempt
    client.subscribe("rwth/cr/PP/CCR/#")  # Subscribe to the topic, receive any messages published on it
    if rc != mqtt.CONNACK_ACCEPTED: # If connection failure
        raise IOError("Connection failure. Check the connection.")


def on_message(client, userdata, msg):  # The callback for when a PUBLISH message is received from the server.
    print("Message received-> " + msg.topic + " " + str(msg.payload))  # Print a received msg
    characters = [chr(ascii) for ascii in msg.payload] # Convert ASCII to char
    chars_joined = ''.join(characters) # Join chars to a string
    received_messages.append(chars_joined) #store as array 
    #splitting the msg
    splitting_list = received_messages
    split_result=[]
    for i in splitting_list:
        split_result+=i.split(":")
    #print(split_result) #for testing

    #combine the msg into array as group of 3
    N = 3
    subList = [split_result[n:n+N] for n in range(0, len(split_result), N)]
    #print(subList) #for testing

    if subList[k][1] == "S1":
        S1.append(subList[k])
        #print(S1)
        angle1.append(subList[k][0])
        #print(angle)
        if(all(x in angle1 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S1.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle1.clear()
            S1.clear()
        else:
            #print("writing")
            with open('S1.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")

    elif subList[k][1] == "S2":
        S2.append(subList[k])
        angle2.append(subList[k][0])
        #print(angle)
        if(all(x in angle2 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S2.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle2.clear()
            S2.clear()
        else:
            #print("writing")
            with open('S2.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")
    
    elif subList[k][1] == "S3":
        S3.append(subList[k])
        angle3.append(subList[k][0])
        #print(angle)
        if(all(x in angle3 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S3.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle3.clear()
            S3.clear()
        else:
            #print("writing")
            with open('S3.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")

    elif subList[k][1] == "S4":
        S4.append(subList[k])
        angle4.append(subList[k][0])
        #print(angle)
        if(all(x in angle4 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S4.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle4.clear()
            S4.clear()
        else:
            #print("writing")
            with open('S4.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")
    
    elif subList[k][1] == "S5":
        S5.append(subList[k])
        angle5.append(subList[k][0])
        #print(angle)
        if(all(x in angle5 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S2.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle5.clear()
            S5.clear()
        else:
            #print("writing")
            with open('S5.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")

    elif subList[k][1] == "S6":
        S6.append(subList[k])
        angle6.append(subList[k][0])
        #print(angle)
        if(all(x in angle6 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S6.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle6.clear()
            S6.clear()
        else:
            #print("writing")
            with open('S6.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")

    elif subList[k][1] == "S7":
        S7.append(subList[k])
        angle7.append(subList[k][0])
        #print(angle)
        if(all(x in angle7 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S7.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle7.clear()
            S7.clear()
        else:
            #print("writing")
            with open('S7.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")

    elif subList[k][1] == "S8":
        S8.append(subList[k])
        angle8.append(subList[k][0])
        #print(angle)
        if(all(x in angle8 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S8.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle8.clear()
            S8.clear()
        else:
            #print("writing")
            with open('S8.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")

    elif subList[k][1] == "S9":
        S9.append(subList[k])
        angle9.append(subList[k][0])
        #print(angle)
        if(all(x in angle9 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S9.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle9.clear()
            S9.clear()
        else:
            #print("writing")
            with open('S9.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")

    elif subList[k][1] == "S10":
        S10.append(subList[k])
        angle10.append(subList[k][0])
        #print(angle)
        if(all(x in angle10 for x in cmpre_list)):
            #print('Empty')
            fileVariable = open('S10.csv',"r+")
            fileVariable.truncate(0)
            fileVariable.close()
            angle10.clear()
            S10.clear()
        else:
            #print("writing")
            with open('S10.csv', 'a+') as f:
                f.write(str(subList[k]) + "\n")


client = mqtt.Client()
client.on_connect = on_connect  # Define callback function for successful connection
client.on_message = on_message  # Define callback function for receipt of a message
# client.connect("m2m.eclipse.org", 1883, 60)  # Connect to (broker, port, keepalive-time)
client.connect(server, 1883,60)
client.loop_forever()  # Start networking daemon
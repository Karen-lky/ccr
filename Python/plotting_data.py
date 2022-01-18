#add on take only the newst angel if multiple repeated
#polar histogram https://stackoverflow.com/questions/63461513/display-real-time-mqtt-data-using-polar-histogram-from-matplotlib

import random
from itertools import count
import pandas as pd
import pandas.io.common
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

#empty list to store variable
angle = []
angle1=[]
angle2=[]
angle3=[]
angle4=[]
angle5=[]
angle6=[]
angle7=[]
angle8=[]
distance = []
distance1 = []
distance2 = []
distance3 = []
distance4 = []
distance5 = []
distance6 = []
distance7 = []
distance8 = []

#plotting (change plot point)
plt.cla()
plt.style.use('fivethirtyeight')

# create a figure with 2x4 subplots
fig, axs = plt.subplots(2, 4)
# intialize line objects (one in each axes)
line1, = axs[0, 0].plot([], [],label='Sensor 1',linestyle='--')
line2, = axs[0, 1].plot([], [], color='r',label='Sensor 2',linestyle='--')
line3, = axs[0, 2].plot([], [], color='g',label='Sensor 3',linestyle='--')
line4, = axs[0, 3].plot([], [], color='c',label='Sensor 4',linestyle='--')
line5, = axs[1, 0].plot([], [], color='m',label='Sensor 5',linestyle='--')
line6, = axs[1, 1].plot([], [], color='y',label='Sensor 6',linestyle='--')
line7, = axs[1, 2].plot([], [], color='k',label='Sensor 7',linestyle='--')
line8, = axs[1, 3].plot([], [], color='brown',label='Sensor 8',linestyle='--')
line = [line1, line2, line3, line4, line5, line6, line7, line8]
#he same axes initalizations as before (just now we do it for both of them)
for ax in axs.flat:
    ax.set_ylim(0, 180)
    ax.set_xlim(0, 400)
    ax.set(xlabel='Distance (cm)', ylabel='Angle (degree)')
    ax.grid()
    ax.legend()

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in axs.flat:
    ax.label_outer()

def animate(i): #for continuous graph
    #empty list to store variable
    angle = []
    angle1=[]
    angle2=[]
    angle3=[]
    angle4=[]
    angle5=[]
    angle6=[]
    angle7=[]
    angle8=[]
    distance = []
    distance1 = []
    distance2 = []
    distance3 = []
    distance4 = []
    distance5 = []
    distance6 = []
    distance7 = []
    distance8 = []

    try:
        data = pd.read_csv('S1.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle1 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance1 = list(map(int, distance))
    except:
        print(" S1.csv is empty and has been skipped.")

    try:
        data = pd.read_csv('S2.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle2 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance2 = list(map(int, distance))
    except:
        print(" S2.csv is empty and has been skipped.")

    try:
        data = pd.read_csv('S3.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle3 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance3 = list(map(int, distance))
    except:
        print(" S3.csv is empty and has been skipped.")

    try:
        data = pd.read_csv('S4.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle4 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance4 = list(map(int, distance))
    except:
        print(" S4.csv is empty and has been skipped.")

    try:
        data = pd.read_csv('S5.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle5 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance5 = list(map(int, distance))
    except:
        print(" S5.csv is empty and has been skipped.")

    try:
        data = pd.read_csv('S6.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle6 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance6 = list(map(int, distance))
    except:
        print(" S6.csv is empty and has been skipped.")

    try:
        data = pd.read_csv('S7.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle7 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance7 = list(map(int, distance))
    except:
        print(" S7.csv is empty and has been skipped.")

    try:
        data = pd.read_csv('S8.csv').values 
        for n in range(len(data)): #for angle data format to int
            new_string = ''.join(char for char in data[n][0] if char.isalnum()) #clear unwanted data
            angle.append(new_string) #make a list from it
        angle8 = list(map(int, angle)) #transfer to int for graph plotting
        for n in range(len(data)): #for distance (the same thing)
            new_string = ''.join(char for char in data[n][2] if char.isalnum()) 
            distance.append(new_string) 
        distance8 = list(map(int, distance))
    except:
        print(" S8.csv is empty and has been skipped.")
    
    # update the data of both line objects
    line[0].set_data(distance1, angle1)
    line[1].set_data(distance2, angle2)
    line[2].set_data(distance3, angle3)
    line[3].set_data(distance4, angle4)
    line[4].set_data(distance5, angle5)
    line[5].set_data(distance6, angle6)
    line[6].set_data(distance7, angle7)
    line[7].set_data(distance8, angle8)

    return line

'''
# create a figure with horizontal subplots
fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8) = plt.subplots(8,1)
# intialize two line objects (one in each axes)
line1, = ax1.plot([], [],label='Sensor 1',linestyle='--')
line2, = ax2.plot([], [], color='r',label='Sensor 2',linestyle='--')
line3, = ax3.plot([], [], color='g',label='Sensor 3',linestyle='--')
line4, = ax4.plot([], [], color='c',label='Sensor 4',linestyle='--')
line5, = ax5.plot([], [], color='m',label='Sensor 5',linestyle='--')
line6, = ax6.plot([], [], color='y',label='Sensor 6',linestyle='--')
line7, = ax7.plot([], [], color='k',label='Sensor 7',linestyle='--')
line8, = ax8.plot([], [], color='brown',label='Sensor 8',linestyle='--')
line = [line1, line2, line3, line4, line5, line6, line7, line8]
#he same axes initalizations as before (just now we do it for both of them)
for ax in [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8]:
    ax.set_ylim(0, 180)
    ax.set_xlim(0, 400)
    ax.set(xlabel='Distance (cm)', ylabel='Angle (degree)')
    ax.grid()
    ax.legend()

# Hide x labels and tick labels for top plots and y ticks for right plots.
for ax in [ax1,ax2, ax3, ax4, ax5, ax6, ax7, ax8]:
    ax.label_outer()
'''

ani = FuncAnimation(fig, animate, blit=True, interval=1000)
#plt.tight_layout()
plt.show()

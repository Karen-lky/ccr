# Collaborative Construction Robots (CCR) Prototyping project

Collaborative construction robots in short C.C.R. is the prototyping project credited by Emre Ergin and Kar Yen Lee in the course of Prototyping Project WS21/22 of Construction & Robotics Masters program at RWTH Aachen. This project is aiming to fill the gap between full automation in the future and manual work in the construction industry of today under a safe collaborative working enviroment. An attachment for industrial robotics arm is prototyped to detect surrounding assets with moving ToF sensors to make the industrial robotic arm more "aware" of its environment and provide safer work environments for human & robot collaboration. 

The CAD model, Microcontroller script, Python script, and Grasshopper script can be found directly in this github repository. These are documented and explained in diffrent folder in the README file or directly commented in the code. And some of the related documents (PPT,documentation, video, ROS code) are also uploaded in google drive under the link https://drive.google.com/drive/folders/1Akr7C4eMUH-XZTfyEK4pEN185Ilmg0Jj?usp=sharing to give better overview of the project.



# CCR Attachment setup

The prototype is designed in a way that it can be fully expanded (or reduced) to serve in different areas of application. CAD Models, microcontroller script and visualization and robot override scripts has been designed & written in a way that any kind of form factor of our prototype is possible to be manufactured just with a change of some basic parameters.

## Cad model

The CAD Model of the attachment has been designed using module components. The _“.f3d”_ models in the provided folders can be used to create the desired form factor for the attachment. In our prototype you will be seeing it in 196cm attachment diameter with 4x4 sensor configuration and 22° radial offset.

![Cad Modules](https://i.imgur.com/UfWhGP3.png)
_*Custom PCB is designed especially for this prototype, might differ for other designs_

_**Motor shaft is a ø6mm brass tube, connection to the “Center Gear” component on Oscillating_Gears.f3z file should be edited in case of the shaft change._

![Assembled Model](https://i.imgur.com/iOuMQkf.png)

## Microcontroller Script

The prototype uses a ESP8266 NodeMCU board to handle faster readings from each sensor and data transmission over wireless network using MQTT. For MQTT handling “EspMQTTClient.h” library and “broker.mqttdashboard.com” broker has been used.  C++ Script setup is as simple as just putting in the number of used sensors and number of XSHUT Pins in the connected order.

```cpp

const int sensor_count = 6;               
int shutdown_pin[sensor_count] = {D3, D0, D4, D5, 1, 3}; 

```
 
Each VL53L0X – ToF Sensor is connected parallelly to the I2C Bus of the NodeMCU Board, corresponding GPIO for Shutdown (XSHUT) and has been powered by a 3.3V voltage regulator with sufficient amps.

![ToF Configuration](https://i.imgur.com/W3QnCzL.png)

Additionally a potentiometer and the motor driver is also connected to board to be able to drive the TT DC Motor and read the angle from the potentiometer. To add more GPIOs on the board, RX and TX pins are disabled for serial communication and transformed to PIN inputs to be able to drive the motor in both directions.

![Motor&Pot Configuration](https://i.imgur.com/rFACMJu.png)

Definitions that are contained in the provided script are:

* `void setID()` - called in setup, assigns new I2C addresses (starting from 0x30) to each Sensor and initializes them
* `void readSensors()` - Reads each sensor one by one and saves distance data in a list
* `void readAngle()` – Reads potentiometer value and maps it to the correct angle, saves in a list
* `void convertJSON_publishMQTT()` - Combines distance and angle lists in a json format and publishes to the given topic (rwth/cr/PP/CCR/Attachment1)  
* `void setMotorDir()` - Reverses motor direction once 0 or 180 degrees on potentiometer has been read

```cpp

void setup() {

  pinMode(1, FUNCTION_3);   // Set RX to GPIO
  pinMode(3, FUNCTION_3);   // Set TX to GPIO

  pinMode(A0, INPUT);       // Potentiometer Input
  pinMode(in1, OUTPUT);     // Motor Dir input 1
  pinMode(in2, OUTPUT);     // Motor Dir input 2

  setID();                  // Setup Sensors    
  
  client.setMaxPacketSize(340); // Set MQTT Data package size

  digitalWrite(in1,LOW);    // Start Motor
  digitalWrite(in2,HIGH);
  
      
}

void loop() { 

  setMotorDir();            // Set direction of motor
  
  client.loop();            // Loop client
 
  readSensors();            // Read sensor values
  
  setMotorDir();            // "Control" Direction once again

  readAngle();              // Read angle value from pot

  convertJSON_publishMQTT();   // convert to JSON and publish
 
}

```

## Visualization Script

For the 3D point cloud visualization and Robot control override, a class called “CCRattachment” has been written in python _CCR_EndeffectorAttachment.py_, which can be initialized by using:

```python

Test1 = CCRAttachment('Emre_0.1', sensor_count=6, sensor_position_offset=22, sensor_divide_half=4)

```


This class consists of multiple definitions to receive the data through MQTT Client and process it for visualization. (More details on how each definition works can be founf under the comments in the script)

* `def save_MQTTdata (topic, payload)` – Listens to the subscribed topic and discriminates the data by the given topic. If the topic is the same with microcontrollers data publishing topic _rwth/cr/PP/CCR/Attachment1_ each unique ‘angle’ data is saved in a global list for each sensor. Once the angle values reaches 0 or 180, the lists are deleted to save next set of values. This definition also listens to CRC local client to get the current TCP state of the used robot, and saves the Frame JSON data _{"X":0,"Y":0,"Z":0,"A":0,"B":0,"C":0}_ in a global variable to later transform all detected points.
* `*def get_Points_orient()` – By using given angle and distance values in each sensors list, creates a point in cartesian coordinates (from polar coordinates) and transforms points based on the sensor configuration as well as the state of the robot.
* `def set_intersectionGeo( min_box=[-1, -1, -1], max_box=[1, 1, 1], det_grnd=True)` – Sets a predefined bounding box in the given environment. The detected points are not considered as “threat” if it falls into given domain, definition of “safe zone”
* `def animate_Plot()` – Animates a frame in matplotlib screen with the given point coordinates
* `def calc_speed()` - Combines and flattens all distance data in all sensors and scans for minimum distance value, this distances is compared to the ISO standards to command the robot to slow down using a CTRL command for Kuka|CRC framework

![Script in action](https://s10.gifyu.com/images/ezgif.com-gif-maker1f5afd07d7718d84.md.gif)

## Grasshopper Component

A custom Grasshopper component has been created to visualise the incoming data through MQTT. This component has been made in addition to main python script, to be used in a "design" environment and visualise the detected assets in a smoother way.

![GH Component](https://i.imgur.com/kAtaxfx.png)

The Component can be used by to preview 2D and 3D visualisation of detected points and interpolate between graphs to create a intermediate 3D point cloud with colorcoded distance values. The resoluton of the point cloud can also be determined.

The component receives MQTT data using various MQTT plugins and visualises similarly to the python code.

_*Direct control of robot through this GH script is not suggested to overwrite the speed since computation and data transfer might take longer_


## ROS package in Google Drive
This is the ROS package to receive distance sensor information and command from robot via MQTT. Then, those and command will be published in the rviz environment for visualiation. The suppoting package behind is ROS noetic version with python 3 in linux system.

![ROS_CCR](https://user-images.githubusercontent.com/77464658/154495988-a71871a6-ce80-4e53-900d-33b52ce9c519.png)


To run the code for intiating the Rviz environment
```
roslaunch kuka_moveit demo.launch
```

To receive MQTT from ToF sensor
```
rosrun kuka_moveit mqtt_get.py
```

To visualize the detected objects in Rviz
```
rosrun kuka_moveit detection_ignore.py
```

To visualize industrial robotics arm motion in Rviz
```
rosrun kuka_moveit motion.py
```
** Helpful links to start with ROS: http://wiki.ros.org/ROS/Tutorials

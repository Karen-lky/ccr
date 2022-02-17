# CCR PT
As a short introduction of this project, collaborative construction robot in short C.C.R. is the prototyping project credited by Emre Ergin and Kar Yen Lee in the course of prototyping driven project WS21/22, RWTH Aachen. This project is strike to fulfill the gap between full automation and manual work in the construction industry under a safe collaborative working enviroment. An attachment for industrial robotics arm is prototyped to detect surrounding assetes with ToF sensor and arduino via MQTT. 

The CAD model, Microcontroller script, Python script, and Grasshopper script can be found directly in this github repository. These are documented and explained in diffrent folder in the README file or directly commented in the code. And some of the related documents (PPT,documentation, video, ROS code) are also uploaded in google drive under the link https://drive.google.com/drive/folders/1Akr7C4eMUH-XZTfyEK4pEN185Ilmg0Jj?usp=sharing to give better overview of the project.

## CAD model 

## Microcontroller script

## Python script

## Grasshopper script

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

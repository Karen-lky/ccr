# CCR PT

This is the documentation for the our prototytping project (WS21/22) and the explanation of code is uploaded in diffrent folder. And some of the related documents (PPT,documentation, video, ROS code) are also uploaded in google drive under the link https://drive.google.com/drive/folders/1Akr7C4eMUH-XZTfyEK4pEN185Ilmg0Jj?usp=sharing.

ive broker from dash (only partly working)

## ROS folder in Google Drive
This is the ROS package to receive distance sensor information and command from robot via MQTT. Then, those  and command will be published in the rviz environment for visualiation. The suppoting package behind is ROS noetic version with python 3 in linux system.

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

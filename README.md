# CCR PT

This is the documentation for the our prototytping project (WS21/22) with the topics collaborative construction robot (C.C.R.) and the explanation of code is uploaded in diffrent folder in the README file or directly commented in the code. And some of the related documents (PPT,documentation, video, ROS code) are also uploaded in google drive under the link https://drive.google.com/drive/folders/1Akr7C4eMUH-XZTfyEK4pEN185Ilmg0Jj?usp=sharing.

## ROS folder in Google Drive
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

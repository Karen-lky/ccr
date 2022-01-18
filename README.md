# CCR PT Visualization

This is the documentation for the our prototytping project (WS21/22) and the explanation of code is uploaded in diffrent folder.

## Arduino folder
sensor_configuration is the script pushed into ESP8266 NodeMCU Microcontroller board. It is configured to set the DC Motor speed through MQTT connection and receive distance value as well as current angle based on the VL53L01 ToF Sensor to publish it the the corresponding MQTT topic. Whole system execution is based on each received speed percentage value from MQTT, which enables the data transmission frequency to be controlled from outside of the microcontroller system by the frequency of sent messages through MQTT.

ToF_Minimum is ...

## Node-red folder
test_interface_node-red is the mock-up for testing environment of the MQTT connection and visualisation


## Python folder
mqttt_get.py is the script to get all the data from the broker server where all the sensors information is being stored.

plotting_data is the script to get live data to analyse the relationship between angle and distance.

plotting_polar is the script to get the polar plot which give better concept visualization for the sensor (the tab continuosly poping out)

plotting_live_dash is the script is similar with plotting_polar but it use live broker from dash (only partly working)





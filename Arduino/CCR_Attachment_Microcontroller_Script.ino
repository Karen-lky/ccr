#include <ArduinoJson.h>

#include "EspMQTTClient.h"                //Simple WIFI & MQTT Library

#include <Adafruit_VL53L0X.h>
#include <Wire.h>                         //Start I2C Bus


const int sensor_count = 6;               // Number of sensors
int shutdown_pin[sensor_count] = {D3, D0, D4, D5, D8, 3};     // Microcontroller input in array {D0, D3, D4, D5 ,D7 ,D8, 3, 1}


EspMQTTClient client(
  "DESKTOP-NQUJCNP 7252",                 // Wifi Name
  "Emrgn1998",                            // Wifi Password
  "broker.mqttdashboard.com",             // MQTT Broker server ip
  "CCRAttachment_Emre",                   // Client name that uniquely identify your device
  1883                                    // The MQTT port, default to 1883. this line can be omitted
);

void onConnectionEstablished(){
  client.publish("rwth/cr/PP/CCR/Validate", "Connection Established");        //Notify on connection established
}


byte address[sensor_count];
int distance[sensor_count];
int angle[sensor_count];


Adafruit_VL53L0X lox[sensor_count];             // Initialize sensor objects
VL53L0X_RangingMeasurementData_t measure;



int in1 = D6;                                  //DC Motor Parameter, DIN direction Control
int in2 = D7;                                  //DC Motor Parameter, DIN direction Control
int enA = 1;                                   //DC Motor Parameter, PWM Speed Control




const int deviation = 14;                      // Angle inconsistency deviation 




void setID() {                                 // Sensor Setup function

  int i;
  for (i=0; i < sensor_count; i++) {
    address[i] = (byte) 0x30 + i;              // Addresses go from 0x30 to 0x37
    pinMode(shutdown_pin[i], OUTPUT);          // Initialized outputs for the board
    digitalWrite(shutdown_pin[i], LOW);         
  }
  delay(10);
  for (i=0; i < sensor_count; i++) {
    digitalWrite(shutdown_pin[i], HIGH);       // Sensor selected to write the adress
    delay(10);
    bool result = lox[i].begin(address[i]);    // Corresponding adress is written
    if(!result) {
      while(1);}                             
  }
  delay(10);
}



void readSensors() {                           // Read all sensors and save to "distance[]" array
  
  for (int i=0; i < sensor_count; i++) {
    float mes_distance;
    lox[i].rangingTest(&measure, false);
    if (measure.RangeStatus != 4) {            // Test if the measurement is valid
      mes_distance = measure.RangeMilliMeter;
      if (mes_distance <= 2000){               // Filter extremes
      distance[i] = mes_distance;}
      else {distance[i] = 2000;}     
    } else {
      distance[i] = 2000;
    }
  }
}



void readAngle() {

  int Angle = map(analogRead(A0),900,210,0,180);
  
  
  if(Angle <= deviation){Angle=0;}                      //set top/bottom limit by deviation for ensuring full half rotation 
  else if (Angle >= 180-deviation){Angle = 180;}
  else {Angle = Angle;} 

    
  for (int i=0; i < sensor_count; i++) {                //Iterate between angle values
  if ((i%2 == 0 && i <=3)||(i%2 == 1 && i >=4))  {      //(i%2 == 0)                     
   angle[i] = 180 - Angle;
    }
   else {                                                                        
    angle[i] = Angle;
    }
  }
}
  


void convertJSON_publishMQTT(){                 
  
  DynamicJsonDocument doc(300);                 // Initialize JSON Document
  char sensor_name[10];                         // set array for sensor names
  char Payload[256];                            // set an array for payload to be published
  for (int i=0; i < sensor_count; i++) {        
        sprintf(sensor_name, "S%d",i+1);
        doc[sensor_name][0] = angle[i];        
        doc[sensor_name][1] = distance[i];    
  }  
 serializeJson(doc, Payload);           
 client.publish("rwth/cr/PP/CCR/Attachment1", Payload);  // Publish the payload
}

void setMotorDir(){

  int Angle_M =  map(analogRead(A0),900,210,0,180);

  //client.publish("rwth/cr/PP/CCR/Attachment1/Angle", String(Angle_M));

  if (Angle_M >= 180 - deviation){
    delay(100);
    digitalWrite(in2,HIGH);
    delay(100);
    digitalWrite(in1,LOW);    
  }
  if (Angle_M <= deviation){
    digitalWrite(in2,LOW);
    delay(100);
    digitalWrite(in1,HIGH);     
  }  
  
  
  }

void setup() {

    
  pinMode(1, FUNCTION_3); 
  pinMode(3, FUNCTION_3);

  pinMode(A0, INPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);   

  setID();    
  
  client.setMaxPacketSize(300);

  digitalWrite(in1,LOW); 
  digitalWrite(in2,HIGH);
  
  //analogWrite(enA,240);                       // Set Motor Speed
      
}

void loop() { 

  setMotorDir();
  
  client.loop();   
 
  readSensors();

  setMotorDir();

  readAngle();

  convertJSON_publishMQTT();   
 
}
  
  

#include "EspMQTTClient.h"                //Simple WIFI & MQTT Library
#include <Wire.h>                         //Start I2C Bus
#include <VL53L0X.h>                      //ToF Sensor Library

VL53L0X sensor;

int enA = D5;                             //DC Motor Parameter, PWM Speed Control
int in1 = D6;                             //DC Motor Parameter, Direction Control 1
int in2 = D7;                             //DC Motor Parameter, Direction Control 2

int pot = A0;

int detectionLimit = 1500;                //Set Detection threshold to minimize errors 

EspMQTTClient client(
  "DESKTOP-NQUJCNP 7252",                 // Wifi Name
  "Emrgn1998",                            // Wifi Password
  "broker.emqx.io",                       // MQTT Broker server ip
  "TestClient",                           // Client name that uniquely identify your device
  1883                                    // The MQTT port, default to 1883. this line can be omitted
);

int speed = 75;


void setup() {
  
  Serial.begin(115200);
  Wire.begin();


  sensor.setTimeout(500);                                                           // Initialize ToF sensor        
  if (!sensor.init())
  {Serial.println("Failed to detect and initialize sensor!");
    while (1) {}}

  sensor.setSignalRateLimit(0.20);                                                  //ToF sensor settings for longer range & accurate detection
  sensor.setVcselPulsePeriod(VL53L0X::VcselPeriodPreRange, 18);
  sensor.setVcselPulsePeriod(VL53L0X::VcselPeriodFinalRange, 14);
  sensor.setMeasurementTimingBudget(20000);

  
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  pinMode(enA, OUTPUT);

  client.enableDebuggingMessages();                                                 // Enable debugging messages sent to serial output
  client.enableHTTPWebUpdater();                                                    // Enable the web updater.


  /*for (int i = 0; i <= 20; i++) {                                                 //initialize motor start to overcome voltage jump
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      analogWrite(enA, 100+i);
      delay(1);
        }*/   
  }


void onConnectionEstablished(){
  client.publish("rwth/cr/esp/PPl/DCcontrol/Validate", "Connection Established");   //Notify on connection established
  
  client.subscribe("rwth/cr/PP/DCcontrol", DC_Motor);                               //Subscribe to the topic
}

    
void loop() {  
  client.loop();                                                                    //Loop the MQTT Client 
}


void DC_Motor(const String & payload){                                              //Start on each message received (QoS 1)

    int speed = payload.toInt();                                                    //Convert string to integer

    int distance = sensor.readRangeSingleMillimeters();                             //Read ToF Sensor, store int under variable
    int angle = map(analogRead(A0),0,1024,0,180);                                   //Detect angle by reading the potentiometer (TBD)
    
    
      if(distance <= 300){                                                          //If too close, slow down the detection (tbd)
       speed = speed * (0.4+(distance/1000));
     }
    else{speed=speed;}

    
      if(distance >= detectionLimit){                                               //If out of range, set to 0
       distance = 0;
     }
    else{distance = distance;}
    
     
     String Distance = String(distance);                                            //Convert DISTANCE to string to be able to publish under given topic     
     String Angle = String(angle);                                                  //Convert ANGLE to string to be able to publish under given topic 
     
     if (sensor.timeoutOccurred()) {Serial.print(" TIMEOUT");                       //In case of ToF Sensor error, print TIMEOUT and light up LED
     digitalWrite(LED_BUILTIN,HIGH);}                       

     String Payload = Angle + ":S1:" + Distance;                                    //STRING Output format for publishing
      
     client.publish("rwth/cr/PP/CCR/Sensor0", Payload);                             //Publish payload to MQTT
     Serial.println(Distance);
     
      
      if(speed >= 1 && speed <= 99){                                                //Send PWM value based on percentage (between 1 and 99)
        digitalWrite(in1, HIGH);
        digitalWrite(in2, LOW);
        analogWrite(enA, map(speed,2,100,100,255));           
        }
      else if (speed == 100) {                                                      //Digital write HIGH to ensure full potential at 100%
        digitalWrite(enA, HIGH);
       }
      else {                                                                        //Digital write LOW to ensure full stop at 0%
        digitalWrite(in1, LOW);
        digitalWrite(in2, LOW);
        digitalWrite(enA,LOW);
        }
 }

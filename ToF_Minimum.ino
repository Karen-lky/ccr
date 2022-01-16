#include <Wire.h>                         //Start I2C Bus
#include <VL53L0X.h>                      //ToF Sensor Library

VL53L0X sensor;                           //Initialize sensor object



int SignalRateLimit = 0.20;               //Sensor Settings
int PeriodPreRange = 18;
int PeriodFinalRange = 14;
int MeasurementTiming = 33000;






void TCA9548A(uint8_t bus){               //Multiplexer thing (might be wrong, or we need maybe something else)
  if(bus > 7) return;
  
Wire.beginTransmission(0x70);
Wire.write(1<<bus);
Wire.endTransmission();}





void setup() {
  
  Serial.begin(115200);
  Wire.begin();

    
  sensor.setTimeout(500);                                                           // Initialize sensor1        
  if (!sensor.init())
  {Serial.print("Failed to detect and initialize sensor: ");
   while (1) {}}
  sensor.setSignalRateLimit(SignalRateLimit);                                       //ToF sensors settings for longer range & accurate detection
  sensor.setVcselPulsePeriod(VL53L0X::VcselPeriodPreRange, PeriodPreRange);
  sensor.setVcselPulsePeriod(VL53L0X::VcselPeriodFinalRange, PeriodFinalRange);
  sensor.setMeasurementTimingBudget(MeasurementTiming);
}

void loop() { 

  int distance = sensor.readRangeSingleMillimeters();
  Serial.print(distance);
  delayMicroseconds(100);
}
  
  

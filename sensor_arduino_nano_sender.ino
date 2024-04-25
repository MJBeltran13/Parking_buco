/************************Hardware Related Macros************************************/
#define MG_PIN              (A6)      // Define analog input channel for CO2 sensor
#define DC_GAIN             (8.5)     // DC gain of amplifier

/***********************Software Related Macros************************************/
#define READ_SAMPLE_INTERVAL    (50)  // Time interval for sampling in normal operation
#define READ_SAMPLE_TIMES       (5)   // Number of samples to take in normal operation

/**********************Application Related Macros**********************************/
#define ZERO_POINT_VOLTAGE     (0.220) // Output of the sensor in volts at 400PPM CO2 concentration
#define REACTION_VOLTGAE       (0.030) // Voltage drop of the sensor when moving from air into 1000ppm CO2

/*****************************Globals***********************************************/
float CO2Curve[3] = {2.602, ZERO_POINT_VOLTAGE, (REACTION_VOLTGAE / (2.602 - 3))};

#include <NewPing.h>

#define SONAR_NUM 2      // Number of ultrasonic sensors
#define MAX_DISTANCE 500 // Maximum distance (in cm) to ping

NewPing sonar[SONAR_NUM] = {   // Sensor object array
  NewPing(5, 6, MAX_DISTANCE),  // Trigger pin, echo pin, and max distance for the first sensor
  NewPing(12, 11, MAX_DISTANCE) // Trigger pin, echo pin, and max distance for the second sensor
};

void setup() {
  Serial.begin(9600); // Initialize serial communication
  Serial.println("Started");
  Serial.println("MG-811 Demonstration");
}

void loop() {
  co2_read();   // Read CO2 levels
  proximity();  // Measure proximity using ultrasonic sensors
  delay(1000);  // Delay between readings
}

void co2_read() {
  float volts = MGRead(MG_PIN); // Read voltage from CO2 sensor
  int percentage = MGGetPercentage(volts, CO2Curve); // Calculate CO2 percentage
  Serial.print("CO2: ");
  if (percentage == -1) {
    Serial.println("400");
  } else {
    Serial.println(percentage);
  }
}

float MGRead(int mg_pin) {
  float v = 0;
  for (int i = 0; i < READ_SAMPLE_TIMES; i++) {
    v += analogRead(mg_pin); // Read analog input
    delay(READ_SAMPLE_INTERVAL);
  }
  v = (v / READ_SAMPLE_TIMES) * 5 / 1024; // Convert to voltage
  return v;
}

int MGGetPercentage(float volts, float *pcurve) {
  if ((volts / DC_GAIN) >= ZERO_POINT_VOLTAGE) {
    return -1; // Sensor value out of range
  } else {
    return pow(10, ((volts / DC_GAIN) - pcurve[1]) / pcurve[2] + pcurve[0]); // Calculate CO2 percentage
  }
}

void proximity() {
  // Ping the first sensor
  int distance_sensor_0 = sonar[0].ping_cm();
  //    Serial.print("Sensor 0: ");
  //    Serial.print(sonar[0].ping_cm());
  //    Serial.println("cm");

  // Ping the second sensor
  int distance_sensor_1 = sonar[1].ping_cm();
  //    Serial.print("Sensor 1: ");
  //    Serial.print(sonar[1].ping_cm());
  //    Serial.println("cm");
  Serial.print("Sensor 0: ");
  // if (distance_sensor_0 < 50) {

  //   Serial.println("1"); // Print '1' if distance is below 50cm
  // } else {
  //   Serial.println("0"); // Print '0' otherwise
  // }
  Serial.print("Sensor 1: ");
//   if (distance_sensor_1 < 50) {
//     Serial.println("1"); // Print '1' if distance is below 50cm
//   } else {
//     Serial.println("0"); // Print '0' otherwise
//   }
}

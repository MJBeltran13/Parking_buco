#include <ESP8266WiFi.h>
#include <espnow.h>

uint8_t broadcastAddress[] = {0x08, 0x3A, 0xF2, 0xC3, 0xE5, 0x2D};

typedef struct struct_message {
  bool a;
  bool b;
  int c;
  bool d;
} struct_message;

// Create a struct_message called myData
struct_message myData;

unsigned long lastTime = 0;
unsigned long timerDelay = 2000;  // send readings timer

// Define global variables for car proximity
int car1 = 0;
int car2 = 0;

// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Last Packet Send Status: ");
  if (sendStatus == 0) {
    Serial.println("Delivery success");
  }
  else {
    Serial.println("Delivery fail");
  }
}

const unsigned int TRIG_PIN_1 = 3; // TRIG pin for first sensor (RX)
const unsigned int ECHO_PIN_1 = 1; // ECHO pin for first sensor (TX)
const unsigned int TRIG_PIN_2 = 13; // TRIG pin for second sensor
const unsigned int ECHO_PIN_2 = 15; // ECHO pin for second sensor
const int BOOL_PIN = 5; // Assign BOOL_PIN to pin number 5 (or any other suitable pin)
const int threshold_distance1 = 50;
const int threshold_distance2 = 50;
unsigned int percentage = 0; // Declare percentage as a global variable


/************************Hardware Related Macros************************************/
const int MG_PIN = A0;

const float DC_GAIN = 8.5;

/***********************Software Related Macros************************************/
const int READ_SAMPLE_INTERVAL = 50;
const int READ_SAMPLE_TIMES = 5;

/**********************Application Related Macros**********************************/
const float ZERO_POINT_VOLTAGE = 0.220;
const float REACTION_VOLTAGE = 0.030;

/*****************************Globals***********************************************/
float CO2Curve[3] = {2.602, ZERO_POINT_VOLTAGE, REACTION_VOLTAGE / (2.602 - 3)};


void setup() {
  // Init Serial Monitor
  Serial.begin(115200);
  pinMode(TRIG_PIN_1, OUTPUT);
  pinMode(ECHO_PIN_1, INPUT);
  pinMode(TRIG_PIN_2, OUTPUT);
  pinMode(ECHO_PIN_2, INPUT);
  pinMode(BOOL_PIN, INPUT);

  // Set device as a Wi-Fi Station
//  WiFi.mode(WIFI_STA);
//
//  // Init ESP-NOW
//  if (esp_now_init() != 0) {
//    Serial.println("Error initializing ESP-NOW");
//    return;
//  }
//
//  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
//  esp_now_register_send_cb(OnDataSent);
//
//  esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
 Serial.println("Started");
}

void loop() {
  proximity();
  co2_read();
  if ((millis() - lastTime) > timerDelay) {
    // Set values to send
    myData.a = car1;   // Assign car1
    myData.b = car2;   // Assign car2
    myData.c = percentage;   // Random value
    myData.d = 1;   // Random value

    // Send message via ESP-NOW
    esp_now_send(broadcastAddress, (uint8_t *) &myData, sizeof(myData));

    lastTime = millis();
  }
}

void proximity() {
  // Sensor 1
  digitalWrite(TRIG_PIN_1, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN_1, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN_1, LOW);

  const unsigned long duration1 = pulseIn(ECHO_PIN_1, HIGH);
  int distance1 = duration1 / 29 / 2;

  // Sensor 2
  digitalWrite(TRIG_PIN_2, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG_PIN_2, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG_PIN_2, LOW);

  const unsigned long duration2 = pulseIn(ECHO_PIN_2, HIGH);
  int distance2 = duration2 / 29 / 2;

  // Output distance readings
  if (distance1 < threshold_distance1) {
    Serial.print("Sensor 1: ");
    Serial.print(distance1);
    Serial.println(" cm");
    car1 = 1; // Set car1 to 1
  } else {
    car1 = 0; // Set car1 to 0
  }

  if (distance2 < threshold_distance2) {
    Serial.print("Sensor 2: ");
    Serial.print(distance2);
    Serial.println(" cm");
    car2 = 1; // Set car2 to 1
  } else {
    car2 = 0; // Set car2 to 0
  }

  delay(100);
}

void co2_read() {
  float volts = MGRead(MG_PIN);
  Serial.print("SEN0159: ");
  Serial.print(volts);
  Serial.print("V\tCO2: ");
  int percentage = MGGetPercentage(volts, CO2Curve);
  Serial.print(percentage);
  Serial.print(" ppm");

  Serial.println();



  delay(500);
}

float MGRead(int mg_pin) {
  float v = 0;
  for (int i = 0; i < READ_SAMPLE_TIMES; i++) {
    v += analogRead(mg_pin);
    delay(READ_SAMPLE_INTERVAL);
  }
  return v / READ_SAMPLE_TIMES * 5 / 1024;
}

int MGGetPercentage(float volts, float *pcurve) {
  if (volts / DC_GAIN >= ZERO_POINT_VOLTAGE) {
    return -1;
  } else {
    return pow(10, ((volts / DC_GAIN) - pcurve[1]) / pcurve[2] + pcurve[0]);
  }
}
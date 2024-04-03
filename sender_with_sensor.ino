#include <ESP8266WiFi.h>
#include <espnow.h>

#define trigPin1 5
#define echoPin1 4
#define trigPin2 7
#define echoPin2 6

long duration1, duration2;
int distance1, distance2;

uint8_t broadcastAddress[] = {0x08, 0x3A, 0x8D, 0xE5, 0xAD, 0x5D};

typedef struct struct_message {
  int a;
  int b;
  int c;
} struct_message;

struct_message myData;

unsigned long lastTime = 0;
unsigned long timerDelay = 2000;

const int MG_PIN = A0;
const float DC_GAIN = 1.0;
const int READ_SAMPLE_INTERVAL = 50;
const int READ_SAMPLE_TIMES = 5;
const float ZERO_POINT_VOLTAGE = 0.165;
const float REACTION_VOLTAGE = 0.030;
float CO2Curve[3] = {2.602, ZERO_POINT_VOLTAGE, REACTION_VOLTAGE / (2.602 - 3)};

void setup() {
  Serial.begin(115200);

  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  WiFi.mode(WIFI_STA);

  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);
  
  esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}

void loop() {
  carDistance(trigPin1, echoPin1, distance1);
  carDistance(trigPin2, echoPin2, distance2);
  int co2Percentage = co2_sensor();

  if ((millis() - lastTime) > timerDelay) {
    myData.a = distance1;
    myData.b = distance2;
    myData.c = co2Percentage;

    esp_now_send(broadcastAddress, (uint8_t *) &myData, sizeof(myData));

    lastTime = millis();
  }
}

void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Last Packet Send Status: ");
  if (sendStatus == 0){
    Serial.println("Delivery success");
  }
  else{
    Serial.println("Delivery fail");
  }
}

void carDistance(int trigPin, int echoPin, int &distance) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(5);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;

  Serial.print("Car Distance = ");
  Serial.print(distance);
  Serial.println(" cm");
  delay(1000); // Delay for readability
}

int co2_sensor() {
  float volts = MGRead(MG_PIN);
  int percentage = MGGetPercentage(volts, CO2Curve);
  Serial.print("CO2: ");
  Serial.print(percentage);
  Serial.println(" ppm");
  delay(500);
  return percentage;
}

float MGRead(int mg_pin) {
  float v = 0;
  for (int i = 0; i < READ_SAMPLE_TIMES; i++) {
    v += analogRead(mg_pin);
    delay(READ_SAMPLE_INTERVAL);
  }
  return v / READ_SAMPLE_TIMES * 3.3 / 1024;
}

int MGGetPercentage(float volts, float *pcurve) {
  if (volts / DC_GAIN >= ZERO_POINT_VOLTAGE) {
    return -1;
  } else {
    return pow(10, ((volts / DC_GAIN) - pcurve[1]) / pcurve[2] + pcurve[0]);
  }
}

#include <ESP8266WiFi.h>
#include <espnow.h>

const int relayPin = 13;

// Structure example to receive data
// Must match the sender structure
typedef struct struct_message {
  int a;
  int b;
  int c;
  int d;
} struct_message;

// Create a struct_message called myData
struct_message myData;

// Callback function that will be executed when data is received
void OnDataRecv(uint8_t *mac, uint8_t *incomingData, uint8_t len) {
  memcpy(&myData, incomingData, sizeof(myData));
  Serial.print(myData.a);
  Serial.print(",");
  Serial.print(myData.b);
  Serial.print(",");
  Serial.print(myData.c);
  Serial.print(",");
  Serial.print(myData.d);
  Serial.println();
}

void setup() {
  // Initialize Serial Monitor
  Serial.begin(9600);
  Serial.println("Begin");

  // Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  // Once ESPNow is successfully Init, we will register for recv CB to
  // get recv packer info
  esp_now_set_self_role(ESP_NOW_ROLE_SLAVE);
  esp_now_register_recv_cb(OnDataRecv);
  Serial.println("End of setup");
}
void loop() {
  Serial.println("Start");
  start();
}
void start() {
  // Perform tasks for 8 hours (28800 seconds)
  unsigned long startTime = millis();
  unsigned long duration = 8 * 60 * 60 * 1000; // 8 hours in milliseconds
  Serial.print("Start at :");
  Serial.println(startTime);
  while (millis() - startTime < duration) {
    unsigned long elapsedTime = millis() - startTime;
    unsigned long remainingTime = duration - elapsedTime;

    Serial.print("Time remaining: ");
    Serial.print(remainingTime / 1000); // Convert milliseconds to seconds
    Serial.println(" seconds");

    digitalWrite(relayPin, LOW);
    delay(1000); // Wait for 1 second
    performTasks();
    delay(1000); // Adjust delay based on your task execution time
    Serial.println("Start");
  }

  // Enter deep sleep for 16 hours
  Serial.println("Start");
  digitalWrite(relayPin, HIGH);
  delay(1000); // Wait for 1 second
  Serial.println("Start");
  ESP.deepSleep(16 * 60 * 60 * 1000000, WAKE_RF_DEFAULT); // Sleep for 16 hours
  Serial.println("Start");
  start();

  // Code below this line will not be executed
}

void performTasks() {
  // Check if there is any incoming data
  if (Serial.available() > 0) {
    // Read the incoming data
    while (Serial.available() > 0) {
      uint8_t data = Serial.read();
      // Process the incoming data as needed
    }
  }
  // Your other task code here
}

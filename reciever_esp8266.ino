#include <ESP8266WiFi.h>
#include <espnow.h>

// Structure to store the message
typedef struct __attribute__((packed)) {
  char text[32];
} message_t;

// Callback function to receive data
void onDataReceived(const uint8_t *mac_addr, const uint8_t *data, int len) {
  Serial.print("Received data from: ");
  Serial.write(mac_addr, 6);
  Serial.print(", Data: ");
  Serial.write(data, len);
  Serial.println();
}

void setup() {
  Serial.begin(115200);

  // Set the ESP8266 to Station mode (client)
  WiFi.mode(WIFI_STA);

  // Initialize ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("ESP-NOW initialization failed");
    return;
  }

  // Register callback function for receiving data
  esp_now_register_recv_cb(onDataReceived);
}

void loop() {
  // Do nothing in the loop, all receiving is handled in onDataReceived
}

#include <ESP8266WiFi.h>
#include <espnow.h>

// Structure to store the message
typedef struct __attribute__((packed)) {
  char text[32];
} message_t;

// Replace this with the MAC address of the receiver ESP8266
uint8_t receiverMacAddress[] = {0x12, 0x34, 0x56, 0x78, 0x9A, 0xBC};

void setup() {
  Serial.begin(115200);

  // Set the ESP8266 to Station mode (client)
  WiFi.mode(WIFI_STA);

  // Initialize ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("ESP-NOW initialization failed");
    return;
  }
}

void loop() {
  // Create a message
  message_t message;
  snprintf(message.text, sizeof(message.text), "Hello from sender");

  // Send the message
  esp_now_send(receiverMacAddress, (uint8_t *) &message, sizeof(message));

  // Wait a bit before sending the next message
  delay(1000);
}

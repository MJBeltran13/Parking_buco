#include <ESP8266WiFi.h>

void setup() {
  Serial.begin(115200);

  // Connect to WiFi
  WiFi.mode(WIFI_STA);
  WiFi.begin("YourWiFiNetwork", "YourWiFiPassword");

  // Wait for connection
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }

  // Print MAC address
  Serial.println("");
  Serial.println("WiFi connected!");
  Serial.print("MAC address: ");
  Serial.println(WiFi.macAddress());
}

void loop() {
  // Nothing to do here
}

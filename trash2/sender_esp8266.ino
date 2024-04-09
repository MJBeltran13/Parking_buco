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

// Callback when data is sent
void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Last Packet Send Status: ");
  if (sendStatus == 0){
    Serial.println("Delivery success");
  }
  else{
    Serial.println("Delivery fail");
  }
}
 
void setup() {
  // Init Serial Monitor
  Serial.begin(115200);
 
  // Set device as a Wi-Fi Station
  WiFi.mode(WIFI_STA);

  // Init ESP-NOW
  if (esp_now_init() != 0) {
    Serial.println("Error initializing ESP-NOW");
    return;
  }

  esp_now_set_self_role(ESP_NOW_ROLE_CONTROLLER);
  esp_now_register_send_cb(OnDataSent);
  
  esp_now_add_peer(broadcastAddress, ESP_NOW_ROLE_SLAVE, 1, NULL, 0);
}
 
void loop() {
  if ((millis() - lastTime) > timerDelay) {
    // Set values to send
    myData.a = random(0, 2);   // Assign 0 or 1 randomly
    myData.b = random(0, 2);   // Assign 0 or 1 randomly
    myData.c = random(0, 21);   // Assign 0 or 1 randomly
    myData.d = random(0, 2);   // Assign 0 or 1 randomly

    // Send message via ESP-NOW
    esp_now_send(broadcastAddress, (uint8_t *) &myData, sizeof(myData));

    lastTime = millis();
  }
}
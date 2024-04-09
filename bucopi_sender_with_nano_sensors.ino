#include <ESP8266WiFi.h>
#include <espnow.h>

uint8_t broadcastAddress[] = {0x08, 0x3A, 0xF2, 0xC4, 0x1D, 0x83};

typedef struct struct_message {
  int a;
  int b;
  int c;
  int d;
} struct_message;

int sensorValue1 = 0;
int sensorValue2 = 0;
int co2Value = 0;

struct_message myData;

unsigned long lastTime = 0;
unsigned long timerDelay = 2000;

void OnDataSent(uint8_t *mac_addr, uint8_t sendStatus) {
  Serial.print("Last Packet Send Status: ");
  if (sendStatus == 0) {
    Serial.println("Delivery success");
  }
  else {
    Serial.println("Delivery fail");
  }
}

void setup() {
  Serial.begin(9600);
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
  read_sensor();
  if ((millis() - lastTime) > timerDelay) {
    // myData.a = sensorValue1;
     if (sensorValue1 < 40) {
      myData.a = 1;
    } else {
      myData.a = 0;
    }

    // myData.b = sensorValue2;
     if (sensorValue2 < 40) {
      myData.b = 1;
    } else {
      myData.b = 0;
    }
    myData.c = co2Value;
    myData.d = 0; // Assigning a default value to indicator

    esp_now_send(broadcastAddress, (uint8_t *) &myData, sizeof(myData));

    lastTime = millis();
  }
}

void read_sensor() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    if (data.startsWith("CO2:")) {
      co2Value = data.substring(5).toInt();
      Serial.print("Received CO2 data: ");
      Serial.println(co2Value);
    } else if (data.startsWith("Sensor 0:")) {
      sensorValue1 = data.substring(data.lastIndexOf(' ') + 1).toInt();
      Serial.print("Received sensor 1 data: ");
      Serial.println(sensorValue1);
    } else if (data.startsWith("Sensor 1:")) {
      sensorValue2 = data.substring(data.lastIndexOf(' ') + 1).toInt();
      Serial.print("Received sensor 2 data: ");
      Serial.println(sensorValue2);
    } else {
      // Handle other data as needed
    }
  }
}

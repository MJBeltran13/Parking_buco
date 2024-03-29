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
    Serial.begin(9600);
    pinMode(BOOL_PIN, INPUT);

    Serial.println("MG-811 Demonstration");
}

void loop() {
    float volts = MGRead(MG_PIN);
    Serial.print("SEN0159: ");
    Serial.print(volts);
    Serial.print("V\tCO2: ");
    int percentage = MGGetPercentage(volts, CO2Curve);
    if (percentage == -1) {
        Serial.print("<400 ppm");
    } else {
        Serial.print(percentage);
        Serial.print(" ppm");
    }
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

// https://wiki.dfrobot.com/CO2_Sensor_SKU_SEN0159
/************************Hardware Related Macros************************************/
#define         MG_PIN                       (A6)     // define which analog input channel you are going to use
#define         DC_GAIN                      (8.5)   // define the DC gain of amplifier

/***********************Software Related Macros************************************/
#define         READ_SAMPLE_INTERVAL         (50)    // define how many samples you are going to take in normal operation
#define         READ_SAMPLE_TIMES            (5)     // define the time interval (in milliseconds) between each sample in
                                                     // normal operation

/**********************Application Related Macros**********************************/
#define         ZERO_POINT_VOLTAGE           (0.220) // define the output of the sensor in volts when the concentration of CO2 is 400PPM
#define         REACTION_VOLTGAE             (0.030) // define the voltage drop of the sensor when moving the sensor from air into 1000ppm CO2

/*****************************Globals***********************************************/
float CO2Curve[3]  =  {2.602, ZERO_POINT_VOLTAGE, (REACTION_VOLTGAE / (2.602 - 3))};
                                                     // two points are taken from the curve.
                                                     // with these two points, a line is formed which is
                                                     // "approximately equivalent" to the original curve.
                                                     // data format: { x, y, slope }; point1: (lg400, 0.324), point2: (lg4000, 0.280)
                                                     // slope = ( reaction voltage ) / (log400 – log1000)

void setup()
{
    Serial.begin(9600);                              // UART setup, baud rate = 9600bps

    Serial.print("MG-811 Demonstration\n");
}

void loop()
{
    float volts;
    int percentage;

    volts = MGRead(MG_PIN);
    Serial.print("SEN0159:");
    Serial.print(volts, 3); // Print with 3 decimal places
    Serial.print("V           ");

    percentage = MGGetPercentage(volts, CO2Curve);
    Serial.print("CO2:");
    if (percentage == -1) {
        Serial.print("400");
    } else {
        Serial.println(percentage);
    }
//    Serial.print(percentage);
    

    delay(500);
}

float MGRead(int mg_pin)
{
    int i;
    float v = 0;

    for (i = 0; i < READ_SAMPLE_TIMES; i++) {
        v += analogRead(mg_pin);
        delay(READ_SAMPLE_INTERVAL);
    }
    v = (v / READ_SAMPLE_TIMES) * 3.9 / 1024; // Adjusted for 3.9V instead of 5V
    return v;
}


int MGGetPercentage(float volts, float *pcurve)
{
    if ((volts / DC_GAIN) >= ZERO_POINT_VOLTAGE) {
        return -1;
    } else {
        return pow(10, ((volts / DC_GAIN) - pcurve[1]) / pcurve[2] + pcurve[0]);
    }
}

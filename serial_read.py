import serial

try:
    # Open serial connection with Arduino
    ser = serial.Serial('COM5', 115200)  # Change 'COM5' to the appropriate port

    # Read data from Arduino and print it
    while True:
        line = ser.readline().decode().strip()  # Read a line of data from serial port
        if line:
            print(line)

except serial.SerialException as e:
    print("An error occurred:", e)

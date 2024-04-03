import serial
import time

# Define the serial port and baud rate
serial_port = 'COM6'  # Change this to match your Arduino's serial port
baud_rate = 115200  # Match the baud rate used in your Arduino sketch

# Create a serial object
ser = serial.Serial(serial_port, baud_rate)

try:
    while True:
        # Read a line from the serial port
        line = ser.readline().decode().strip()
        
        # Check if the line is not empty
        if line:
            # Split the line by spaces to extract individual values
            values = line.split()
            # Check if the line contains all expected values
            if len(values) == 4:
                car1 = int(values[0])
                car2 = int(values[1])
                co2 = int(values[2])
                indicator = int(values[3])
                print("car 1: ", car1)
                print("car 2: ", car2)
                print("co2: ", co2)
                print("indicator: ", indicator)
                print()
            else:
                print("Invalid data format:", line)
            
        # Optional: Add a small delay to prevent high CPU usage
        time.sleep(0.1)

except KeyboardInterrupt:
    # If the user presses Ctrl+C, close the serial port
    ser.close()

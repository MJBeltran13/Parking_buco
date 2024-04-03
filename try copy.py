import serial

# Open the serial port
ser = serial.Serial('COM6', 115200)  # Change 'COM6' to the appropriate port on your system

def read_sensor_values():
    sensor_values = {}
    line = ser.readline().decode().strip()  # Read a line from serial and decode
    print("Received:", line)  # Print received line for debugging
    pairs = line.split(",")  # Split the line into key-value pairs
    for pair in pairs:
        key, value = pair.split(":")  # Split each pair into key and value
        sensor_values[key.strip()] = value.strip()  # Remove leading/trailing whitespace
    return sensor_values

# Example usage:
while True:
    data = read_sensor_values()
    car_1_value = data.get('a', 'Not Found')
    car_2_value = data.get('b', 'Not Found')
    co2_value = data.get('c', 'Not Found')
    indicator_value = data.get('d', 'Not Found')
    print("Car 1:", car_1_value)
    print("Car 2:", car_2_value)
    print("CO2:", co2_value)
    print("Indicator:", indicator_value)

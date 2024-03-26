from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# Creating the database engine
engine = create_engine('sqlite:///spartan_dataset.db', echo=True)

# Creating a base class for our models
Base = declarative_base()

# Define the model for saving arrays
class ArrayData(Base):
    __tablename__ = 'array_data'

    id = Column(Integer, primary_key=True)
    data = Column(String)  # Storing array as text

# Define the model for CO2 sensor data
class CO2SensorData(Base):
    __tablename__ = 'co2_sensor_data'

    id = Column(Integer, primary_key=True)
    sensor_name = Column(String)
    co2_level = Column(Float)

# Creating tables
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to save array data
def save_array_data(data):
    data_json = json.dumps(data)  # Serialize array to JSON
    new_data = ArrayData(data=data_json)
    session.add(new_data)
    session.commit()

# Function to save CO2 sensor data
def save_co2_sensor_data(sensor_name, co2_level):
    new_data = CO2SensorData(sensor_name=sensor_name, co2_level=co2_level)
    session.add(new_data)
    session.commit()

# Save array data
save_array_data([1, 1, 1, 1, 1])

# Save CO2 sensor data
save_co2_sensor_data("Sensor1", 350.5)
save_co2_sensor_data("Sensor2", 400.2)

# Query and print array data
array_data = session.query(ArrayData).all()
print("Array Data:")
for data in array_data:
    print(f"ID: {data.id}, Data: {json.loads(data.data)}")

# Query and print CO2 sensor data
co2_sensor_data = session.query(CO2SensorData).all()
print("\nCO2 Sensor Data:")
for data in co2_sensor_data:
    print(f"ID: {data.id}, Sensor Name: {data.sensor_name}, CO2 Level: {data.co2_level}")

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Creating the database engine
engine = create_engine('sqlite:///example.db', echo=True)

# Creating a base class for our models
Base = declarative_base()

# Define the model for CO2 sensor data
class CO2SensorData(Base):
    __tablename__ = 'co2_sensor_data'

    id = Column(Integer, primary_key=True)
    sensor_name = Column(String)
    co2_level = Column(Float)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to fetch all CO2 sensor data
def get_all_co2_sensor_data():
    return session.query(CO2SensorData).all()

# Fetching all CO2 sensor data
co2_sensor_data = get_all_co2_sensor_data()
print("\nCO2 Sensor Data:")
for data in co2_sensor_data:
    print(f"ID: {data.id}, Sensor Name: {data.sensor_name}, CO2 Level: {data.co2_level}")

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

# Creating tables
Base.metadata.create_all(engine)

# Creating a session
Session = sessionmaker(bind=engine)
session = Session()

# Function to save CO2 sensor data
def save_co2_sensor_data(sensor_name, co2_level):
    new_data = CO2SensorData(sensor_name=sensor_name, co2_level=co2_level)
    session.add(new_data)
    session.commit()

# Save CO2 sensor data
save_co2_sensor_data("Sensor1", 10.5)
save_co2_sensor_data("Sensor2", 12.2)

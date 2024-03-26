from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# Creating the database engine
engine = create_engine('sqlite:///example.db', echo=True)

# Creating a base class for our models
Base = declarative_base()

# Define the model for saving arrays
class ArrayData(Base):
    __tablename__ = 'array_data'

    id = Column(Integer, primary_key=True)
    data = Column(String)  # Storing array as text

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

# Save array data
save_array_data([0, 0, 0, 0, 0])

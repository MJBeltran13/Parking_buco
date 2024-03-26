from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json
from datetime import datetime


# Create a SQLAlchemy engine
engine = create_engine(
    "sqlite:///sample_database.db", echo=True
)  # Use 'echo=True' for logging

# Create a base class for declarative class definitions
Base = declarative_base()


# Define your model
class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True)
    sample_array = Column(String)
    date_created = Column(DateTime, default=datetime.now)


# Create the database schema
Base.metadata.create_all(engine)

# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Populate the database with the sample_array
sample_array = [
    1,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
    1,
    1,
    23,
    21,
    "safe",
]

sample_json = json.dumps(sample_array)

sample_row = Sample(sample_array=sample_json)
session.add(sample_row)

# Commit the changes
session.commit()

# Close the session
session.close()

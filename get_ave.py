from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timedelta

# Creating the SQLAlchemy engine
engine = create_engine("sqlite:///sample.db", echo=True)

# Creating a session class
Session = sessionmaker(bind=engine)

# Creating a base class for our declarative class
Base = declarative_base()


# Defining our SQLAlchemy model
class Sample(Base):
    __tablename__ = "samples"

    id = Column(Integer, primary_key=True)
    data = Column(String)
    date_added = Column(DateTime, default=datetime.now)


# Function to get the values saved on yesterday at the 42nd index
def get_values_at_42nd_index_for_yesterday():
    # Calculate the datetime for yesterday
    yesterday = datetime.now() - timedelta(days=1)

    # Calculate the start and end datetime for yesterday
    start_of_day = datetime(yesterday.year, yesterday.month, yesterday.day, 0, 0, 0)
    end_of_day = datetime(yesterday.year, yesterday.month, yesterday.day, 23, 59, 59)

    # Creating a session
    with Session() as session:
        # Querying the sample data for yesterday
        samples = (
            session.query(Sample)
            .filter(Sample.date_added >= start_of_day, Sample.date_added <= end_of_day)
            .all()
        )

        # Extracting the data values at index 42
        values = []
        for sample in samples:
            data = sample.data.split(",")
            if len(data) > 42:
                values.append(int(data[42]))

        return values


# Function to calculate the average of a list of values
def calculate_average(values):
    if values:
        return sum(values) / len(values)
    else:
        return None


# Example usage: Get values for yesterday
values = get_values_at_42nd_index_for_yesterday()
average_value = calculate_average(values)

if average_value is not None:
    print(average_value)
else:
    print("No data available for yesterday.")

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


# Function to get the value saved yesterday at the 44th index
def get_value_at_44th_index_saved_yesterday():
    # Calculate the datetime for yesterday
    yesterday = datetime.now() - timedelta(days=1)

    # Creating a session
    with Session() as session:
        # Querying the sample data saved yesterday
        sample = (
            session.query(Sample)
            .filter(Sample.date_added >= yesterday)
            .order_by(Sample.date_added.desc())
            .first()
        )

        # Extracting the data value
        if sample:
            data = sample.data.split(',')
            value = data[42] if len(data) > 42 else None
            print("Value saved yesterday at index 42:", value)
        else:
            print("No data saved yesterday.")


# Call the function to get the value saved yesterday
get_value_at_44th_index_saved_yesterday()

# [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1,345, 32, "unsafe"]
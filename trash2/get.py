from sqlalchemy import create_engine, Column, Integer, String, DateTime, desc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

Base = declarative_base()

class Sample(Base):
    __tablename__ = 'samples'

    id = Column(Integer, primary_key=True)
    data = Column(String)
    date_added = Column(DateTime, default=datetime.now)

engine = create_engine('sqlite:///sample.db', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def get_latest_data_from_db():
    latest_record = session.query(Sample).order_by(desc(Sample.date_added)).first()
    if latest_record:
        return json.loads(latest_record.data)
    else:
        return None

latest_data = get_latest_data_from_db()
print("Latest data:", latest_data)

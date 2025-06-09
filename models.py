from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Widget(Base):
    __tablename__ = "widgets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(64), nullable=False)
    number_of_parts = Column(Integer, nullable=False)
    created_date = Column(DateTime, default=datetime.utcnow)
    updated_date = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

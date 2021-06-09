from sqlalchemy import Column, DateTime, Integer, String, Text

from database import Base

class History(Base):
    __tablename__ = "storage_history"

    id = Column(Integer, primary_key=True, index=True)
    version = Column(Integer, unique=False, index=True)
    date = Column(DateTime, index=True)
    user = Column(String(150))
    changed_data = Column(Text)

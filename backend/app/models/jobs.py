from sqlalchemy import Column, Integer, String, DateTime
from app.database.session import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    company = Column(String, index=True)
    title = Column(String)
    status = Column(String)
    date_applied = Column(DateTime)
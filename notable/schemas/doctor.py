from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from notable.db.base_class import Base
from sqlalchemy.ext.declarative import declarative_base



class Doctor(Base):
    __tablename__ = "doctor"
    id = Column(Integer, primary_key = True, nullable = False)
    first_name = Column(String(256), nullable = False)
    last_name = Column(String(256), nullable = False)
    appointment = relationship(
        "Appointment",
        cascade = "all,delete-orphan",
        back_populates = "doctor",
        uselist = True
        )

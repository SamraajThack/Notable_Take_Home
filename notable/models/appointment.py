from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship
from notable.db.base_class import Base





class Appointment(Base):
    __tablename__ = 'appointment'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(256), nullable = False)
    last_name = Column(String(256), nullable = False)
    date  = Column(String(256), nullable = False)
    time = Column(String(256), nullable = False)
    kind = Column(String(256), nullable = False)
    doctor_id = Column(Integer, ForeignKey("doctor.id"))
    doctor = relationship("Doctor", back_populates = "appointment")

    

from sqlalchemy.orm import Session
from notable.models.appointment import Appointment
from notable.models.doctor import Doctor
from notable.schemas import appointment, doctor
from fastapi.encoders import jsonable_encoder



def create_appointment(db: Session, appointment: appointment.AppointmentCreate):
    obj_in_data = jsonable_encoder(appointment)
    db_item = Appointment(**obj_in_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_all_doctors(db: Session):
    return db.query(Doctor).all()

def get_appointment_by_day_doc(db: Session, *, doc_id: int, date: str):
    return db.query(Appointment).join(Doctor, Appointment.doctor_id == Doctor.id).with_entities(Appointment).filter(Doctor.id == doc_id).filter(Appointment.date == date).all()

def get_appointment(db: Session, appointment_id: int):
    return db.query(Appointment).filter(Appointment.id == appointment_id).first()

def remove_appointment(db: Session, appointment_id: int):
    obj = db.query(Appointment).get(appointment_id)
    db.delete(obj)
    db.commit()
    return obj


def get_appointment_by_time_doc(db: Session, time: str, date: str, doc_id: int):
    return db.query(Appointment).join(Doctor, Appointment.doctor_id == Doctor.id).with_entities(Appointment.id).filter(Doctor.id == doc_id).filter(Appointment.time == time).filter(Appointment.date == date).all()



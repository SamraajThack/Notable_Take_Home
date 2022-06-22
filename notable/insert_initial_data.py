
from notable.schemas import appointment, doctor
from fastapi import Depends
from sqlalchemy.orm import Session
from notable.models.appointment import Appointment
from notable.models.doctor import Doctor
from fastapi.encoders import jsonable_encoder
from notable.db.session import SessionLocal

import logging
from notable.initial_data import appointments, doctors

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def init() -> None:
    db = SessionLocal()
    insert_initial_data(db = db, appointments = appointments, doctors = doctors)

def insert_initial_data(db: Session, appointments: appointment.AppointmentInsertList, doctors: doctor.DoctorInsertList):
    for doc in doctors:
        obj_json = jsonable_encoder(doc)
        db_item = Doctor(**obj_json)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        
    for app in appointments:
        obj_json = jsonable_encoder(app)
        db_item = Appointment(**obj_json)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
    
    


    return {"Success"}

def main():
    logger.info("Creating initial data in DB")
    init()
    logger.info("Initial data created")

if __name__ == "__main__":
    main()
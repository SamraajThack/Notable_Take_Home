from fastapi import Depends, FastAPI, APIRouter, HTTPException
import uvicorn
import subprocess
from sqlalchemy.orm import Session
from notable.db.session import SessionLocal
from notable.schemas.appointment import Appointment, AppointmentCreate, AppointmentResults
from notable.schemas.doctor import Doctor, DoctorResults
from notable.crud import crud_utils
from datetime import datetime






app = FastAPI(Title = "Notable API", openapi_url = "/openapi.json")
api_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def start():
    cmd = ['python', 'notable/main.py']
    subprocess.run(cmd)

@api_router.get('/', status_code = 200)
def root():
    return {"message": "Hello Notable!"}

@api_router.post('api/appointment', status_code = 200, response_model = Appointment)
def create_appoinment(*, app: AppointmentCreate, db: Session =  Depends(get_db)):

    #check is the time is valid 
    time_arr = [int(i) for i in app.time.split(":")]
    if time_arr[1]%15 != 0:
        #error 
        raise HTTPException(
            status_code =406, detail = "Invalid time, please use 15 minute intervals"
        )

    num_appointments = list(crud_utils.get_appointment_by_time_doc(db = db, time = app.time, doc_id = app.doctor_id, date = app.date))
    print(num_appointments)
    if len(num_appointments) >= 3:
        raise HTTPException(
            status_code = 406, detail = "Doctor has too many appointments at this time, please chose another time or day"
        )
    else:    
        new_app =  crud_utils.create_appointment(db=db, appointment = app)
        return new_app.__dict__

@api_router.get('api/doctors', status_code = 200, response_model = DoctorResults)
def get_all_doctors(db: Session = Depends(get_db)):
    doctors_list = crud_utils.get_all_doctors(db = db)
    if not doctors_list:
        raise HTTPException(
            status_code = 404, detail = "No doctors"
        )
    return {"doctors": doctors_list}


@api_router.get('api/appointments/{app_id}', status_code = 200, response_model = Appointment)
def get_appointment(*, app_id:int, db: Session = Depends(get_db)):
    single_appointment =  crud_utils.get_appointment(db=db, appointment_id = app_id)
    if not single_appointment:
        raise HTTPException(
            status_code = 404, detail = "No appointment found"
        )
    return single_appointment.__dict__

@api_router.get('api/doctors/{doc_id}/{date}', status_code = 200, response_model = AppointmentResults)
def get_appointments_for_the_day_for_doctor(*, doc_id: int, date: str, db: Session = Depends(get_db)):

    appointment_list = crud_utils.get_appointment_by_day_doc(db = db, doc_id = doc_id, date = date)
    if not appointment_list:
        raise HTTPException(
            status_code = 404, detail = "No appointments found"
        )
    
    appointments = []
    for app in appointment_list:
        appointments.append(app.__dict__)
    
    return {"appointments" : appointments}

@api_router.delete('api/appointments/{app_id}', status_code = 200, response_model = Appointment)
def delete_appointment(*, app_id, db: Session = Depends(get_db)):
    single_appointment =  crud_utils.get_appointment(db=db, appointment_id = app_id)
    if not single_appointment:
        raise HTTPException(
            status_code = 404, detail = "No appointment found"
        )
    deleted =  crud_utils.remove_appointment(db = db , appointment_id = app_id)
    return deleted.__dict__


app.include_router(api_router)

# if __name__ == "__main__":
#     uvicorn.run("main:app", host = "127.0.0.1", port= 8001, log_level = "debug", reload = True)
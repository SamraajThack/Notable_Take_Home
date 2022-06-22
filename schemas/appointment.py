from pydantic import BaseModel
from typing import Sequence

class AppointmentBase(BaseModel):
    first_name : str
    last_name : str
    date : str
    time : str
    kind : str
    doctor_id : int

class AppointmentCreate(AppointmentBase):
    pass

class AppointmentInDBBase(BaseModel):
    id: int
    doctor_id: int

    class Config:
        orm_mode = True

class Appointment(AppointmentBase):
    pass

class AppointmentInsert(AppointmentBase):
    id : int

class AppointmentInsertList(BaseModel):
    results: Sequence[AppointmentInsert]

class AppointmentResults(BaseModel):
    appointments: Sequence[Appointment]


    
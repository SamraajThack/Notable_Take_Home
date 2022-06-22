
from pydantic import BaseModel
from typing import Sequence


class DoctorBase(BaseModel):
    # id: int
    first_name : str
    last_name : str

class DoctorCreate(DoctorBase):
    pass

class DoctorInDBBase(DoctorBase):
    id : int

    class Config:
        orm_mode = True

class Doctor(DoctorInDBBase):
    pass

class DoctorInDB(DoctorInDBBase):
    pass

class DoctorInsert(DoctorBase):
    id : int

class DoctorInsertList(BaseModel):
    result : Sequence[DoctorInsert]

class DoctorResults(BaseModel):
    doctors : Sequence[Doctor]
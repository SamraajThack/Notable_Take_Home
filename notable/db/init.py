
from notable.db.session import engine
from notable.db.base import Base, Appointment, Doctor

def init_db():
    Base.metadata.create_all(bind=engine)


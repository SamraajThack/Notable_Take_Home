from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLAlCHEMY_DATABASE_URI = "sqlite:///example.db"

engine = create_engine(
    SQLAlCHEMY_DATABASE_URI,
    connect_args = {"check_same_thread": False},
)

SessionLocal =sessionmaker(autocommit=False, autoflush=False, bind=engine)

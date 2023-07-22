from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://qbv81sqvscp0x5b3r61o:pscale_pw_Fs4bMDHifg3xAKWEUFZsWvs6s93aorfFanq63mg9gWh@aws.connect.psdb.cloud/mobirace"

engine=create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

SessionLocal = sessionmaker(autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
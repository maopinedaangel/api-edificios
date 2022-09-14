from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

#DATABASE_URL = "postgresql://postgres:Admin123@localhost:5432/edificios"
#DATABASE_URL = os.environ['DATABASE_URL']
DATABASE_URL = "postgresql://vifdriwsarlgnn:06aff5e4a25040c88559624062aca29f87e07a5462a28d77d646c0cb9384297b@ec2-34-233-64-238.compute-1.amazonaws.com:5432/d19npbm96rbsqa"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()
Base.metadata.schema = "edificios_schema"
from sqlalchemy.orm import sessionmaker
from models import db, Base

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=db)

Base.metadata.create_all(bind=db)

def get_db():
    session = LocalSession() #create a session
    try:
        yield session
    finally:
        session.close() #close the session
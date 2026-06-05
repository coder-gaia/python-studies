from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    
    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )
    
    name = Column(String)
    email = Column(String)
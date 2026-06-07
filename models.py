from sqlalchemy import Column, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
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

    tasks = relationship(
        "Task",
        back_populates="user",
        cascade="all, delete"
    )


class Task(Base):
    __tablename__ = "tasks"

    id = Column(
        String,
        primary_key=True,
        default=lambda: str(uuid.uuid4())
    )

    title = Column(String)
    completed = Column(Boolean, default=False)

    user_id = Column(
        String,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="tasks"
    )
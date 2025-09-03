from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    name=Column(String(30), nullable=False)
    email=Column(String(255),nullable=False,unique=True)
    username=Column(String(50),nullable=False,unique=True)
    password=Column(String(255),nullable=False)

    cars=relationship("Car",back_populates="user")
    addresses=relationship("Address",back_populates="user",cascade="all, delete-orphan")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "username": self.username
        }



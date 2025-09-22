from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from .base import Base


class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    username=Column(String(50),nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    role=Column(String(20),nullable=False)

    invoices=relationship("Invoice",back_populates="user")
    contacts=relationship("Contact",back_populates="user")

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "role": self.role
        }



from sqlalchemy import Column,Integer,String,ForeignKey,Date
from sqlalchemy.orm import relationship
from .base import Base


class Contact(Base):
    __tablename__="contacts"

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    name=Column(String(255),nullable=False)
    phone=Column(String(20),nullable=True)
    email=Column(String(255),nullable=True)

    user=relationship("User",back_populates="contacts")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "name": self.name,
            "phone": self.phone,
            "email": self.email
        }
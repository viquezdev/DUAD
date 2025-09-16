from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Car(Base):
    __tablename__="cars"

    id=Column(Integer,primary_key=True)
    make=Column(String(50),nullable=False)
    model=Column(String(50),nullable=False)
    year=Column(Integer,nullable=False)

    user_id=Column(Integer,ForeignKey("users.id",ondelete="SET NULL"),nullable=True)

    user=relationship("User",back_populates="cars")
    
    def to_dict(self):
        return {
            "id": self.id,
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "user_id": self.user_id
        }
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Address(Base):
    __tablename__="Addresses"

    id=Column(Integer,primary_key=True)
    street=Column(String(100),nullable=False)
    city=Column(String(50),nullable=False)
    postal_code=Column(String(10))
    country=Column(String(50))
    
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    user=relationship("User",back_populates="addresses")
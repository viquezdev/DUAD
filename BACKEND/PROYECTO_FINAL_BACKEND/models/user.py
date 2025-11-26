from  sqlalchemy import  Column, Integer,String,Boolean,DateTime,func
from sqlalchemy.orm import relationship
from .base import Base

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    username=Column(String(50),nullable=False,unique=True)
    password=Column(String(255),nullable=False)
    email=Column(String(255),nullable=False,unique=True)
    is_admin=Column(Boolean,nullable=False,default=False)
    created_at=Column(DateTime,default=func.now())
    updated_at=Column(DateTime,default=func.now())

    shopping_carts=relationship("ShoppingCart",back_populates="user")
    invoices=relationship("Invoice",back_populates="user")
    login_history = relationship("LoginHistory", back_populates="user")

    def to_dict(self):
        return{
            "id":self.id,
            "username":self.username,
            "email":self.email,
            "is_admin":self.is_admin,
            "created_at":self.created_at,
            "updated_at":self.updated_at
        }

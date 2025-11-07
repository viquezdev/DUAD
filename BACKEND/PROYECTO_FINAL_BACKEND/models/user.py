from  sqlalchemy import  Column, Integer,String,Boolean,DateTime,func
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



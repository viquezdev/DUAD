from sqlalchemy import Column,Integer,String,Numeric,Text
from .base import Base


class Product(Base):
    __tablename__="products"
    id=Column(Integer, primary_key=True)
    sku=Column(String(100),nullable=False,unique=True)
    name=Column(String(100),nullable=False)
    price=Column(Numeric(10,2),nullable=False)
    description=Column(Text)
    quantity=Column(Integer,nullable=False,default=0)

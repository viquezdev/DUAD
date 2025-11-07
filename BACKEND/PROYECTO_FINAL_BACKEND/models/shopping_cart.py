from sqlalchemy import Column,Integer,String,DateTime,ForeignKey,func
from .base import Base


class ShoppingCart(Base):
    __tablename__="shopping_carts"
    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    status=Column(String(50),nullable=False,default='active')
    created_at=Column(DateTime,default=func.now())

    

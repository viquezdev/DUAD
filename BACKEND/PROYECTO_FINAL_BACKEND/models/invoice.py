from sqlalchemy import Column,Integer,String,DateTime,func,Numeric,ForeignKey
from .base import Base


class Invoice(Base):
    __tablename__="invoices"

    id=Column(Integer,primary_key=True)
    invoice_number=Column(String(100),nullable=False,unique=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    shopping_cart_id=Column(Integer,ForeignKey("shopping_carts.id"),nullable=False)
    created_at=Column(DateTime,default=func.now())
    billing_address=Column(String(255),nullable=False)
    payment_method=Column(String(50),nullable=False)
    payment_status=Column(String(50),nullable=False)
    total_amount=Column(Numeric(10,2),nullable=False)

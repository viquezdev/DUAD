from sqlalchemy import Column,Integer,String,DateTime,func,Numeric,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base


class Invoice(Base):
    __tablename__="invoices"

    id=Column(Integer,primary_key=True)
    invoice_number=Column(String(100),nullable=False,unique=True)
    user_id=Column(Integer,ForeignKey("users.id",onupdate="CASCADE",ondelete="SET NULL"),nullable=True)
    shopping_cart_id=Column(Integer,ForeignKey("shopping_carts.id",onupdate="CASCADE",ondelete="SET NULL"),nullable=True)
    created_at=Column(DateTime,default=func.now())
    billing_address=Column(String(255),nullable=False)
    payment_method=Column(String(50),nullable=False)
    payment_status=Column(String(50),nullable=False)
    total_amount=Column(Numeric(10,2),nullable=False)

    user=relationship("User",back_populates="invoices")
    shopping_cart=relationship("ShoppingCart",back_populates="invoice")

    returns=relationship("Return",back_populates="invoice")

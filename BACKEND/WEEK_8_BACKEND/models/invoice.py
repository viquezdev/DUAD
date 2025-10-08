from sqlalchemy import Column,Integer,String,ForeignKey,Numeric,Date
from sqlalchemy.orm import relationship
from .base import Base


class Invoice(Base):
    __tablename__="invoices"

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    total_amount=Column(Numeric(10,2),nullable=False)
    invoice_date=Column(Date,nullable=False)

    user=relationship("User",back_populates="invoices")
    invoice_products=relationship("InvoiceProducts",back_populates="invoice")
    products=relationship("Product",secondary="invoice_products",viewonly=True)
    
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "total_amount": self.total_amount,
            "invoice_date": self.invoice_date
        }
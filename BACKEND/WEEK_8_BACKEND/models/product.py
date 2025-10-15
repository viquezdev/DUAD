from sqlalchemy import Column,Integer,String,ForeignKey,Numeric,Date
from sqlalchemy.orm import relationship
from .base import Base


class Product(Base):
    __tablename__="products"

    id=Column(Integer,primary_key=True)
    name=Column(String(50),nullable=False)
    price=Column(Numeric(10,2),nullable=False)
    entry_date=Column(Date,nullable=False)
    quantity=Column(Integer,nullable=False)

    invoice_products=relationship("InvoiceProducts",back_populates="product")
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": float(self.price),
            "entry_date": self.entry_date.isoformat(),
            "quantity": self.quantity
        }
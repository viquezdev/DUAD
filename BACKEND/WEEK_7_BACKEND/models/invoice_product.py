from sqlalchemy import Column,Integer,ForeignKey,Numeric
from sqlalchemy.orm import relationship
from .base import Base


class InvoiceProducts(Base):
    __tablename__="invoice_products"

    id=Column(Integer,primary_key=True)
    invoice_id=Column(Integer,ForeignKey("invoices.id"),nullable=False)
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    quantity=Column(Integer,nullable=False)
    subtotal=Column(Numeric(10,2),nullable=False)

    product=relationship("Product",back_populates="invoice_products")
    invoice=relationship("Invoice",back_populates="invoice_products")
    def to_dict(self):
        return {
            "id": self.id,
            "invoice_id": self.invoice_id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "subtotal": self.price
        }
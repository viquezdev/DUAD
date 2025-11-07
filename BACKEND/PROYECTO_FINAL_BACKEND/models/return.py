from sqlalchemy import Column,Integer,Boolean,DateTime,func,Numeric,ForeignKey,Text
from .base import Base


class Return(Base):
    __tablename__="returns"

    id=Column(Integer,primary_key=True)
    invoice_id=Column(Integer,ForeignKey("invoices.id"),nullable=False)
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    quantity_returned=Column(Integer,nullable=False)
    return_date=Column(DateTime,default=func.now())
    reason=Column(Text)
    processed=Column(Boolean,nullable=False,default=False)
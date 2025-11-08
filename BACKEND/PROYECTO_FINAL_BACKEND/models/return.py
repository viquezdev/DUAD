from sqlalchemy import Column,Integer,Boolean,DateTime,func,Numeric,ForeignKey,Text
from sqlalchemy.orm import relationship
from .base import Base


class Return(Base):
    __tablename__="returns"

    id=Column(Integer,primary_key=True)
    invoice_id=Column(Integer,ForeignKey("invoices.id",onupdate="CASCADE",ondelete="SET NULL"),nullable=True)
    product_id=Column(Integer,ForeignKey("products.id",onupdate="CASCADE",ondelete="SET NULL"),nullable=True)
    quantity_returned=Column(Integer,nullable=False)
    return_date=Column(DateTime,default=func.now())
    reason=Column(Text)
    processed=Column(Boolean,nullable=False,default=False)

    invoice=relationship
    product=
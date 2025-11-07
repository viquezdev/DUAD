from sqlalchemy import Column,Integer,Numeric,ForeignKey
from .base import Base

class ShoppingCartProduct(Base):
    __tablename__="shopping_cart_products"

    id=Column(Integer,primary_key=True)
    shopping_cart_id=Column(Integer,ForeignKey("shopping_carts.id"),nullable=False)
    product_id=Column(Integer,ForeignKey("products.id"),nullable=False)
    quantity=Column(Integer,nullable=False)
    subtotal=Column(Numeric(10,2),nullable=False)
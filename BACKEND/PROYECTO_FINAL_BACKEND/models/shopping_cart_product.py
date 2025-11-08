from sqlalchemy import Column,Integer,Numeric,ForeignKey
from sqlalchemy.orm import relationship
from .base import Base

class ShoppingCartProduct(Base):
    __tablename__="shopping_cart_products"

    id=Column(Integer,primary_key=True)
    shopping_cart_id=Column(Integer,ForeignKey("shopping_carts.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False)
    product_id=Column(Integer,ForeignKey("products.id",onupdate="CASCADE",ondelete="CASCADE"),nullable=False,)
    quantity=Column(Integer,nullable=False)
    subtotal=Column(Numeric(10,2),nullable=False)

    product=relationship("Product", back_populates="shopping_cart_products")
    shopping_cart=relationship("ShoppingCart",back_populates="shopping_cart_products")
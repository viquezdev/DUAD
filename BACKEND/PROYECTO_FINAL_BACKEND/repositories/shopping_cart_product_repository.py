from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models.shopping_cart_product import ShoppingCartProduct
from db import SessionLocal

class ShoppingCartProductRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

        def create(self,shopping_cart_id,product_id,quantity,subtotal):
            pass

        def update(self,id,shopping_cart_id=None,product_id=None,quantity=None,subtotal=None):
            pass

        def delete(self):
            pass

        def get_all(self):
            pass

        def get_by_shopping_cart_id(self,shopping_cart_id):
            pass

        def get_by_product_id(self,product_id):
            pass



        
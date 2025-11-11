from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models.product import  Product
from db import SessionLocal

class ProductRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

        def create(self,sku,name,price,description,quantity):
            pass

        def update(self,id,sku=None,name=None,price=None,description=None,quantity=None):
            pass

        def delete(self):
            pass

        def get_all(self):
            pass

        def get_by_id(self,product_id):
            pass

        def get_by_sku(self,sku):
            pass

        def get_by_name(self,name):
            pass

        
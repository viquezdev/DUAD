from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models.shopping_cart import ShoppingCart
from db import SessionLocal

class ShoppingCartRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

        def create(self,user_id,status,created_at):
            pass

        def update(self,id,user_id=None,status=None,created_at=None):
            pass

        def delete(self):
            pass

        def get_all(self):
            pass

        def get_by_user_id(self,user_id):
            pass

        def get_by_status(self,status):
            pass




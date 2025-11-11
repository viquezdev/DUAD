from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models.returns import Returns
from db import SessionLocal

class ReturnsRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

        def create(self,invoice_id,product_id,quantity_returned,return_date,reason,processed):
            pass

        def update(self,id,invoice_id=None,product_id=None,quantity_returned=None,return_date=None,reason=None,processed=None):
            pass

        def delete(self):
            pass

        def get_all(self):
            pass

        def get_by_invoice_id(self,invoice_id):
            pass

        def get_by_product_id(self,product_id):
            pass



    
    
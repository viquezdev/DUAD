from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models.invoice import Invoice
from db import SessionLocal

class InvoiceRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

        def create(self,invoice_number,user_id,shopping_cart_id,created_at,billing_address,payment_method,payment_status,total_amount):
            pass

        def update(self,id,invoice_number=None,user_id=None,shopping_cart_id=None,created_at=None,billing_address=None,payment_method=None,payment_status=None,total_amount=None):
            pass

        def delete(self):
            pass

        def get_all(self):
            pass

        def get_by_invoice_number(self,invoice_number):
            pass

        def get_by_user_id(self,user_id):
            pass

        def get_by_shopping_cart_id(self,shopping_cart_id):
            pass

    
    
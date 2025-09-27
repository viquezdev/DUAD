
from sqlalchemy.exc import SQLAlchemyError
from models.user import User
from db import SessionLocal
from models.invoice import Invoice

class InvoiceRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory


    def create(self, user_id,total_amount,invoice_date):
        
        try:
            with self.session_factory() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                
                invoice=Invoice(
                        user_id=user_id,
                        total_amount=total_amount,
                        invoice_date=invoice_date
                    )  
            
                session.add(invoice)
                session.commit()
                session.refresh(invoice)
                return invoice
        except SQLAlchemyError as e:
            print(f"Error creating invoice : {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                invoices= session.query(Invoice).all()
                return invoices
        except SQLAlchemyError as e:
            print(f"Error fetching invoices: {e}")
            return []


    def get_by_id(self,invoice_id):
        
        try:
            with self.session_factory() as session:
                invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if invoice:
                    return invoice
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching invoice by id {invoice_id}: {e}")
            return None
        
    def get_by_user(self,user_id):
        
        try:
            with self.session_factory() as session:
                invoices=session.query(Invoice).filter_by(user_id=user_id).all()
                if invoices:
                    return invoices
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching contacts: {e}")
            return None
        
    def get_user_id(self,invoice_id):
        
        try:
            with self.session_factory() as session:
                invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if invoice:
                    return invoice.user_id
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching invoice by id {invoice_id}: {e}")
            return None
        

    def update(self,invoice_id,total_amount=None,invoice_date=None):
        
        try:
            with self.session_factory() as session:    
                invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if not invoice:
                    return None
                
                fields = {
                "total_amount": total_amount,
                "invoice_date": invoice_date
                }

                for attr, value in fields.items():
                    if value is not None:
                        setattr(invoice, attr, value)
                session.commit()
                session.refresh(invoice)
                return invoice

        except SQLAlchemyError as e:
            print(f"Error updating invoice : {e}")
            return None
            
    
    def delete(self,invoice_id):
        
        try:
            with self.session_factory() as session:    
                invoice =session.query(Invoice).filter_by(id=invoice_id).one_or_none() 
                if not invoice:
                    return None
                session.delete(invoice)
                session.commit()
                return invoice
        except SQLAlchemyError as e:
            print(f"Error deleting invoice : {e}")
            return None
        

    def update_totals(self):
        try:
            with self.session_factory() as session:
                invoices = session.query(Invoice).all()
                for invoice in invoices:
                    total = sum(item.subtotal for item in invoice.invoice_products)
                    invoice.total_amount = total
                session.commit()
                return True
        except SQLAlchemyError as e:
            print(f"DB error: {e}")
            return False


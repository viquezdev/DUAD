from sqlalchemy.exc import SQLAlchemyError
from models.invoice import Invoice
from models.user import User
from models.shopping_cart import ShoppingCart
from repositories.shopping_cart_product_repository import ShoppingCartProductRepository
from db.db import SessionLocal

class InvoiceRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory


    def create(self,invoice_number,user_id,shopping_cart_id,created_at,billing_address,payment_method,payment_status,total_amount):
        try:
            with self.session_factory() as session:
                found_invoice=session.query(Invoice).filter_by(invoice_number=invoice_number).one_or_none()
                if found_invoice:
                    print(f"The invoice number already exists")
                    return None 
                found_user=session.query(User).filter_by(id=user_id).one_or_none()
                if not found_user:
                    print(f"User with id {user_id} not found.")
                    return None
                found_shopping_cart=session.query(ShoppingCart).filter_by(id=shopping_cart_id).one_or_none()
                if not found_shopping_cart:
                    print(f"Shopping cart with id {shopping_cart_id} not found.")
                    return None
                invoice=Invoice(
                    invoice_number=invoice_number,
                    user_id=user_id,
                    shopping_cart_id=shopping_cart_id,
                    created_at=created_at,
                    billing_address=billing_address,
                    payment_method=payment_method,
                    payment_status=payment_status,
                    total_amount=total_amount
                    )
                session.add(invoice)
                session.commit()
                session.refresh(invoice)
                return invoice   
        except SQLAlchemyError as e:
            print(f"Error creating invoice: {e}")


    def update(self,id,invoice_number=None,user_id=None,shopping_cart_id=None,created_at=None,billing_address=None,payment_method=None,payment_status=None,total_amount=None):
        try:
            with self.session_factory() as session:
                found_invoice=session.query(Invoice).filter_by(id=id).one_or_none()
                if not found_invoice:
                    return None
                if user_id:
                    found_user=session.query(User).filter_by(id=user_id).one_or_none()
                    if not found_user:
                        print(f"User with id {user_id} not found.")
                        return None
                if shopping_cart_id:
                    found_shopping_cart=session.query(ShoppingCart).filter_by(id=shopping_cart_id).one_or_none()
                    if not found_shopping_cart:
                        print(f"Shopping cart with id {shopping_cart_id} not found.")
                        return None  
                fields={
                    "invoice_number":invoice_number,
                    "user_id":user_id,
                    "shopping_cart_id":shopping_cart_id,
                    "created_at":created_at,
                    "billing_address":billing_address,
                    "payment_method":payment_method,
                    "payment_status":payment_status,
                    "total_amount":total_amount
                }
                for attr,value in fields.items():
                    if value is not None:
                        setattr(found_invoice,attr,value)
                session.commit()
                session.refresh(found_invoice)
                return found_invoice
        except SQLAlchemyError as e:
            print(f"Error updating invoice: {e}")
        

    def delete(self,invoice_id):
        try:
            with self.session_factory() as session:
                found_invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if not found_invoice:
                    print(f"Invoiced with id {id} not found.")
                    return None
                session.delete(found_invoice)
                session.commit()
                return found_invoice
        except SQLAlchemyError as e:
            print(f"Error deleting invoice: {e}")


    def get_all(self):
        try:
            with self.session_factory() as session:
                invoices=session.query(Invoice).all()
                return invoices
        except SQLAlchemyError as e:
            print(f"Error fetching invoices: {e}")
            return []
        

    def get_by_id(self,invoice_id):
        try:
            with self.session_factory() as session:
                invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if not invoice:
                    return None
                return invoice
        except SQLAlchemyError as e:
            print(f"Error fetching invoice by id {invoice_id}: {e}")
            return None


    def get_by_invoice_number(self,invoice_number):
        try:
            with self.session_factory() as session:
                invoice=session.query(Invoice).filter_by(invoice_number=invoice_number).one_or_none()
                return invoice
        except SQLAlchemyError as e:
            print(f"Error fetching invoice: {e}")
            return []


    def get_by_user_id(self,user_id):
        try:
            with self.session_factory() as session:
                invoices=session.query(Invoice).filter_by(user_id=user_id).all()
                return invoices
        except SQLAlchemyError as e:
            print(f"Error fetching invoices: {e}")
            return []


    def get_by_shopping_cart_id(self,shopping_cart_id):
        try:
            with self.session_factory() as session:
                invoice=session.query(Invoice).filter_by(shopping_cart_id=shopping_cart_id).one_or_none()
                return invoice
        except SQLAlchemyError as e:
            print(f"Error fetching invoice: {e}")
            return []
        
    
    def calculate_total(self,shopping_cart_id):
        try:
            total=0
            shopping_cart_product_repo=ShoppingCartProductRepository()
            items=shopping_cart_product_repo.get_by_shopping_cart_id(shopping_cart_id)
            for item in items:
                total+=item.subtotal
            return total
        except Exception as e:
            print(f"Error calculating total: {e}")

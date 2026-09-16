from sqlalchemy.exc import SQLAlchemyError
from models.invoice import Invoice
from models.user import User
from models.shopping_cart import ShoppingCart
from sqlalchemy.orm import joinedload
from repositories.shopping_cart_product_repository import ShoppingCartProductRepository
from db.db import SessionLocal
import uuid
from datetime import datetime

class InvoiceRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

    def generate_invoice_number(self):
        date = datetime.now().strftime("%Y%m%d")
        unique_id = uuid.uuid4().hex[:8].upper()
        return f"FAC-{date}-{unique_id}"

    def create(
    self,
    user_id,
    shopping_cart_id,
    billing_address,
    payment_method,
    payment_status,
    total_amount,
    full_name,
    phone_number,
    email
    ):
        try:
            with self.session_factory() as session:

                found_user = session.query(User).filter_by(
                    id=user_id
                ).one_or_none()

                if not found_user:
                    print(f"User with id {user_id} not found.")
                    return None

                found_shopping_cart = session.query(ShoppingCart).filter_by(
                    id=shopping_cart_id
                ).one_or_none()

                if not found_shopping_cart:
                    print(
                        f"Shopping cart with id {shopping_cart_id} not found."
                    )
                    return None

                invoice_number = self.generate_invoice_number()

                invoice = Invoice(
                    invoice_number=invoice_number,
                    user_id=user_id,
                    shopping_cart_id=shopping_cart_id,
                    billing_address=billing_address,
                    payment_method=payment_method,
                    payment_status=payment_status,
                    total_amount=total_amount,
                    full_name=full_name,
                    phone_number=phone_number,
                    email=email
                )

                session.add(invoice)
                session.commit()
                session.refresh(invoice)

                return invoice

        except SQLAlchemyError as e:
            print(f"Error creating invoice: {e}")
            return None


    def update(self,id,invoice_number=None,user_id=None,shopping_cart_id=None,created_at=None,billing_address=None,payment_method=None,payment_status=None,total_amount=None,full_name=None,phone_number=None,email=None):
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
                    "total_amount":total_amount,
                    "full_name":full_name,
                    "phone_number":phone_number,
                    "email":email
                }
                for attr,value in fields.items():
                    if value is not None:
                        setattr(found_invoice,attr,value)
                session.flush()
                return found_invoice
        except SQLAlchemyError as e:
            print(f"Error updating invoice: {e}")
            return None
        

    def delete(self,invoice_id):
        try:
            with self.session_factory() as session:
                found_invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if not found_invoice:
                    print(f"Invoiced with id {id} not found.")
                    return None
                session.delete(found_invoice)
                session.commit()
                session.flush()
                
                return found_invoice
        except SQLAlchemyError as e:
            print(f"Error deleting invoice: {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                invoices = (
                    session.query(Invoice)
                    .options(joinedload(Invoice.user))
                    .all()
                )
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

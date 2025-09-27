
from sqlalchemy.exc import SQLAlchemyError
from models.invoice import Invoice
from models.product import Product
from models.invoice_product import InvoiceProducts
from db import SessionLocal

class InvoiceProductsRepository:
    def __init__(self, session_factory=SessionLocal):
        self.session_factory = session_factory


    def create(self, invoice_id, product_id, quantity, subtotal):
        try:
            with self.session_factory() as session:
                invoice = session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if not invoice:
                    return None
                
                product = session.query(Product).filter_by(id=product_id).one_or_none()
                if not product:
                    return None
                
                invoice_product = InvoiceProducts(
                    invoice_id=invoice_id,
                    product_id=product_id,
                    quantity=quantity,
                    subtotal=subtotal
                )
                session.add(invoice_product)
                session.commit()
                session.refresh(invoice_product)
                return invoice_product
        except SQLAlchemyError as e:
            print(f"Error creating invoice product: {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                return session.query(InvoiceProducts).all()
        except SQLAlchemyError as e:
            print(f"Error fetching invoice products: {e}")
            return []


    def get_by_id(self, invoice_product_id):
        try:
            with self.session_factory() as session:
                return session.query(InvoiceProducts).filter_by(id=invoice_product_id).one_or_none()
        except SQLAlchemyError as e:
            print(f"Error fetching invoice product by id {invoice_product_id}: {e}")
            return None


    def get_by_invoice(self, invoice_id):
        try:
            with self.session_factory() as session:
                return session.query(InvoiceProducts).filter_by(invoice_id=invoice_id).all()
        except SQLAlchemyError as e:
            print(f"Error fetching products for invoice {invoice_id}: {e}")
            return []


    def update(self, invoice_product_id, invoice_id=None, product_id=None, quantity=None, subtotal=None):
        try:
            with self.session_factory() as session:
                invoice_product = session.query(InvoiceProducts).filter_by(id=invoice_product_id).one_or_none()
                if not invoice_product:
                    return None
                
                if invoice_id:
                    invoice = session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                    if not invoice:
                        return None
                    invoice_product.invoice_id = invoice_id

                if product_id:
                    product = session.query(Product).filter_by(id=product_id).one_or_none()
                    if not product:
                        return None
                    invoice_product.product_id = product_id

                if quantity is not None:
                    invoice_product.quantity = quantity
                if subtotal is not None:
                    invoice_product.subtotal = subtotal

                session.commit()
                session.refresh(invoice_product)
                return invoice_product
        except SQLAlchemyError as e:
            print(f"Error updating invoice product: {e}")
            return None


    def delete(self, invoice_product_id):
        try:
            with self.session_factory() as session:
                invoice_product = session.query(InvoiceProducts).filter_by(id=invoice_product_id).one_or_none()
                if not invoice_product:
                    return None
                session.delete(invoice_product)
                session.commit()
                return invoice_product
        except SQLAlchemyError as e:
            print(f"Error deleting invoice product: {e}")
            return None


    def delete_by_invoice_and_product(self, invoice_id, product_id):
        try:
            with self.session_factory() as session:
                invoice_product = session.query(InvoiceProducts).filter_by(
                    invoice_id=invoice_id, product_id=product_id
                ).one_or_none()
                if not invoice_product:
                    return None
                session.delete(invoice_product)
                session.commit()
                return invoice_product
        except SQLAlchemyError as e:
            print(f"Error deleting invoice product {invoice_id}-{product_id}: {e}")
            return None

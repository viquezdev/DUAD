
from sqlalchemy.exc import SQLAlchemyError
from models.user import User
from db import SessionLocal
from models.invoice import Invoice
from models.product import Product
from models.invoice_product import InvoiceProducts

class InvoiceProductsRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory


    def create(self, invoice_id,product_id,quantity,subtotal):
        
        try:
            with self.session_factory() as session:
                invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if not invoice:
                    return None
                
                product=session.query(Product).filter_by(id=product_id).one_or_none()
                if not product:
                    return None
                
                invoice_products=InvoiceProducts(
                    invoice_id=invoice_id,
                    product_id=product_id,
                    quantity=quantity,
                    subtotal=subtotal
                    )  
            
                session.add(invoice_products)
                session.commit()
                session.refresh(invoice_products)
                return invoice
        except SQLAlchemyError as e:
            print(f"Error creating invoice : {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                invoice_products= session.query(InvoiceProducts).all()
                return invoice_products
        except SQLAlchemyError as e:
            print(f"Error fetching invoices: {e}")
            return []


    def get_by_id(self,invoice_products_id):
        
        try:
            with self.session_factory() as session:
                invoice_products=session.query(InvoiceProducts).filter_by(id=invoice_products_id).one_or_none()
                if invoice_products:
                    return invoice_products
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching invoice by id {invoice_products_id}: {e}")
            return None
        

    def update(self,invoice_product_id,invoice_id,product_id,quantity,subtotal):
        
        try:
            with self.session_factory() as session:    
                invoice_products=session.query(InvoiceProducts).filter_by(id=invoice_product_id).one_or_none()
                if not invoice_products:
                    return None
                
                invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                if not invoice:
                    return None
                
                product=session.query(Product).filter_by(id=product_id).one_or_none()
                if not product:
                    return None
                
                fields = {
                "invoice_id": invoice_id,
                "product_id": product_id,
                "quantity": quantity,
                "subtotal": subtotal
                }

                for attr, value in fields.items():
                    if value is not None:
                        setattr(invoice_products, attr, value)
                session.commit()
                session.refresh(invoice_products)
                return invoice_products

        except SQLAlchemyError as e:
            print(f"Error updating invoice : {e}")
            return None
            
    
    def delete(self,invoice_products_id):
        
        try:
            with self.session_factory() as session:    
                invoice_products =session.query(InvoiceProducts).filter_by(id=invoice_products_id).one_or_none() 
                if not invoice_products:
                    return None
                session.delete(invoice_products)
                session.commit()
                return invoice_products
        except SQLAlchemyError as e:
            print(f"Error deleting invoice : {e}")
            return None

""" 
    def get_addresses_with_street():
        try:
            with SessionLocal() as session:
                addresses= session.query(Address).filter(Address.street.ilike("%street%")).all()
                return [address.to_dict() for address in addresses]
        except SQLAlchemyError as e:
            print(f"Error fetching addresses: {e}")
            return []

"""


from sqlalchemy.exc import SQLAlchemyError
from models.returns import Return
from  models.invoice import Invoice
from models.product import Product
from db import SessionLocal

class ReturnsRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

#CUANDO CREO EL RETORNO DEBO ACTUALIZAR LA CANTIDAD DE PRODUCTOS RETORNADOS , PODRIA CREAR UN METODO EN PRODUCT_REPOSITORY PARA ACTUALIZAR INVENTARIO
        def create(self,invoice_id,product_id,quantity_returned,return_date,reason,processed):
            try:
                with self.session_factory() as session:
                    found_invoice=session.query(Invoice).filter_by(id=invoice_id).one_or_none()
                    if not found_invoice:
                        print(f"Invoice with id {invoice_id} not found")
                        return None
                    found_product=session.query(Product).filter_by(id=product_id).one_or_none()
                    if not found_product:
                        print(f"Product with id {product_id} not found")
                        return None
                    new_return=Return(
                        invoice_id=invoice_id,
                        product_id=product_id,
                        quantity_returned=quantity_returned,
                        return_date=return_date,
                        reason=reason,
                        processed=processed
                        )
                    session.add(new_return)
                    session.commit()
                    session.refresh(new_return)
                    return new_return
            except SQLAlchemyError as e:
                print(f"Error creating return: {e}")


        def update(self,id,invoice_id=None,product_id=None,quantity_returned=None,return_date=None,reason=None,processed=None):
            try:
                with self.session.factory() as session:
                    found_return=session.query(Return).filter_by(id=id).one_or_none()
                    if not found_return:
                        print(f"Return with id {id} not found.")
                        return None
                    if invoice_id:
                        found_invoice=session.query(Invoice).filter_by(id=id).one_or_none()
                        if not found_invoice:
                            print(f"Invoice with id {invoice_id} not found.")
                            return None
                    if product_id:
                        found_product=session.query(Product).filter_by(id=product_id).one_or_none()
                        if not found_product:
                            print(f"Product with id {product_id} not found.")
                            return None
                    fields={
                        "invoice_id":invoice_id,
                        "product_id":product_id,
                        "quantity_returned":quantity_returned,
                        "return_date":return_date,
                        "reason":reason,
                        "processed":processed
                    }
                    for attr,value in fields.items():
                        if value is not None:
                            setattr(found_return,attr,value)
                    session.commit()
                    session.refresh(found_return)
            except SQLAlchemyError as e:
                print(f"Error updating return: {e}")
        

        def delete(self,return_id):
            try:
                with self.session_factory() as session:
                    found_return=session.query(Return).filter_by(id=return_id).one_or_none()
                    if not found_return:
                        print(f"Return with id {id} not found.")
                        return None
                    session.delete(found_return)
                    session.commit()
                    return found_return
            except SQLAlchemyError as e:
                print(f"Error deleting return: {e}")


        def get_all(self):
            try:
                with self.session_factory() as session:
                    returns=session.query(Return).all()
                    return returns
            except SQLAlchemyError as e:
                print(f"Error fetching returns: {e}")
                return []


        def get_by_invoice_id(self,invoice_id):
            try:
                with self.session_factory() as session:
                    found_returns=session.query(Return).filter_by(invoice_id=invoice_id).all()
                    return found_returns
            except SQLAlchemyError as e:
                print(f"Error fetching returns: {e}")
                return []


        def get_by_product_id(self,product_id):
            try:
                with self.session_factory() as session:
                    found_returns=session.query(Return).filter_by(product_id=product_id).all()
                    return found_returns
            except SQLAlchemyError as e:
                print(f"Error fetching returns: {e}")
                return []



    
    
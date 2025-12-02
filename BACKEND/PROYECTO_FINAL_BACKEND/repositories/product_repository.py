
from sqlalchemy.exc import SQLAlchemyError
from models.product import  Product
from db.db import SessionLocal

class ProductRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory


    def create(self,sku,name,price,description,quantity):
        try:
            with self.session_factory() as session:
                product_sku_verify=session.query(Product).filter_by(sku=sku).one_or_none()
                if product_sku_verify:
                    return None
                product=Product(
                    sku=sku,
                    name=name,
                    price=price,
                    description=description,
                    quantity=quantity
                    )
                session.add(product)
                session.commit()
                session.refresh(product)
                return product
        except SQLAlchemyError as e:
            print(f"Error creating product: {e}")
            return None


    def update(self,id,sku=None,name=None,price=None,description=None,quantity=None):
        try:
            with self.session_factory() as session:
                product=session.query(Product).filter_by(id=id).one_or_none()
                product_sku_verify=session.query(Product).filter_by(sku=sku).one_or_none()
                if not product:
                    print(f"Product with id {id} not found.")
                    return None
                if product_sku_verify:
                    print(f"Product with sku {sku} not found.")
                    return None
                fields={
                    "sku":sku,
                    "name":name,
                    "price":price,
                    "description":description,
                    "quantity":quantity
                }
                for attr,value in fields.items():
                    if value is not None:
                        setattr(product,attr,value)
                session.commit()
                session.refresh(product)
                return product
        except SQLAlchemyError as e:
            print(f"Error updating product: {e}")
            return None


    def delete(self,id):
        try:
            with self.session_factory() as session:
                product=session.query(Product).filter_by(id=id).one_or_none()
                if not product:
                    return None
                session.delete(product)
                session.commit()
                return product
        except SQLAlchemyError as e:
            print(f"Error deleting product: {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                products=session.query(Product).all()
                return products
        except SQLAlchemyError as e:
            print(f"Error fetching products: {e}")
            return []


    def get_by_id(self,id):
        try:
            with self.session_factory() as session:
                    product=session.query(Product).filter_by(id=id).one_or_none()
                    if not product:
                        return None
                    return product
        except SQLAlchemyError as e:
            print(f"Error fetching product by id {id}: {e}")
            return None
    
        
    def get_by_sku(self,sku):
        try:
            with self.session_factory() as session:
                    product=session.query(Product).filter_by(sku=sku).one_or_none()
                    if not product:
                        return None
                    return product
        except SQLAlchemyError as e:
            print(f"Error fetching product by sku {sku}: {e}")
            return None


    def get_by_name(self,name):
        try:
            with self.session_factory() as session:
                    product=session.query(Product).filter_by(name=name).one_or_none()
                    if not product:
                        return None
                    return product
        except SQLAlchemyError as e:
            print(f"Error fetching product by name {name}: {e}")
            return None

        
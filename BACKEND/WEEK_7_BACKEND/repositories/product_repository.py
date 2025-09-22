
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.product import Product
from db import SessionLocal

class ProductRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory
        

    def create(self,name,price,entry_date,quantity):
        try:
            
            product=Product(
                    name=name,
                    price=price,
                    entry_date=entry_date,
                    quantity=quantity
                )  
            with self.session_factory() as session:
                session.add(product)
                session.commit()
                session.refresh(product)
                return product
        except SQLAlchemyError as e:
            print(f"Error creating product : {e}")
            return None

    
    def get_all(self):
        try:
            with self.session_factory() as session:
                products=session.query(Product).all()
                return products
        except SQLAlchemyError as e:
            print(f"Error fetching products: {e}")
            return []


    def get_by_id(self,product_id):
        
        try:
            with self.session_factory() as session:
                product=session.query(Product).filter_by(id=product_id).one_or_none()
                if product:
                    return product
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching product by id {product_id}: {e}")
            return None


    def update(self,product_id,name=None,price=None,entry_date=None,quantity=None):
        
        try:
            with self.session_factory() as session:    
                product=session.query(Product).filter_by(id=product_id).one_or_none()
                if not product:
                    return None
                
                fields = {
                "name": name,
                "price": price,
                "entry_date": entry_date,
                "quantity": quantity

                }
                
                for attr, value in fields.items():
                    if value is not None:
                        setattr(product, attr, value)
                session.commit()
                session.refresh(product)
                return product

        except SQLAlchemyError as e:

            print(f"Error updating product: {e}")
            return None
    
    
    def delete(self,product_id):
        
        try:
            with self.session_factory() as session:
                product =session.query(Product).filter_by(id=product_id).one_or_none()
                if not product:
                    return None
                session.delete(product)
                session.commit()
                return product
        except SQLAlchemyError as e:
            print(f"Error deleting car : {e}")
            return None


    # @staticmethod
    # def assign_to_user(car_id,user_id):
    
    #     try:
    #         with SessionLocal() as session:    
    #             car=session.query(Car).filter_by(id=car_id).one_or_none()
    #             if not car:
    #                 return None
    #             user=session.query(User).filter_by(id=user_id).one_or_none()
    #             if not user:
    #                 return None
    #             car.user_id=user.id
    #             session.commit()
    #             session.refresh(car)
    #             return car.to_dict()

    #     except SQLAlchemyError as e:
    #         print(f"Error assigning car to user: {e}")
    #         return None
        

    # @staticmethod
    # def get_cars_without_users():
    #     try:
        #     with SessionLocal() as session:
        #         cars=session.query(Car).filter(Car.user_id==None).all()
        #         return [car.to_dict() for car in cars]
        # except SQLAlchemyError as e:
        #     print(f"Error fetching cars: {e}")
        #     return []


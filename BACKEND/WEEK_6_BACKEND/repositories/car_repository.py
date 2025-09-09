
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.car import Car
from models.user import User
from db import SessionLocal

class CarRepository:
    
    @staticmethod
    def create(make,model,year,user_id=None):
        try:
            with SessionLocal() as session:
                if user_id is not None:
                    user=session.query(User).filter_by(id=user_id).one_or_none()
                    if not user:
                        return None

                car=Car(
                        make=make,
                        model=model,
                        year=year,
                        user_id=user_id
                    )  
            
                session.add(car)
                session.commit()
                session.refresh(car)
                return car
        except SQLAlchemyError as e:
            print(f"Error creating car : {e}")
            return None

    
    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                cars=session.query(Car).all()
                return [car.to_dict() for car in cars]
        except SQLAlchemyError as e:
            print(f"Error fetching cars: {e}")
            return []

    
    @staticmethod
    def get_by_id(car_id):
        
        try:
            with SessionLocal() as session:
                car=session.query(Car).filter_by(id=car_id).one_or_none()
                if car:
                    return car.to_dict()
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching car by id {car_id}: {e}")
            return None


    @staticmethod    
    def update(car_id,make=None,model=None,year=None):
        
        try:
            with SessionLocal() as session:    
                car=session.query(Car).filter_by(id=car_id).one_or_none()
                if not car:
                    return None
                
                fields = {
                "make": make,
                "model": model,
                "year": year
                }
                
                for attr, value in fields.items():
                    if value is not None:
                        setattr(car, attr, value)
                session.commit()
                session.refresh(car)
                return car

        except SQLAlchemyError as e:

            print(f"Error updating car : {e}")
            return None
    
    
    @staticmethod
    def delete(car_id):
        
        try:
            with SessionLocal() as session:
                car =session.query(Car).filter_by(id=car_id).one_or_none()
                if not car:
                    return None
                session.delete(car)
                session.commit()
                return car
        except SQLAlchemyError as e:
            print(f"Error deleting car : {e}")
            return None


    @staticmethod
    def assign_to_user(car_id,user_id):
    
        try:
            with SessionLocal() as session:    
                car=session.query(Car).filter_by(id=car_id).one_or_none()
                if not car:
                    return None
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                car.user_id=user.id
                session.commit()
                session.refresh(car)
                return car.to_dict()

        except SQLAlchemyError as e:
            print(f"Error assigning car to user: {e}")
            return None
        

    @staticmethod
    def get_cars_without_users():
        try:
            with SessionLocal() as session:
                cars=session.query(Car).filter(Car.user_id==None).all()
                return [car.to_dict() for car in cars]
        except SQLAlchemyError as e:
            print(f"Error fetching cars: {e}")
            return []


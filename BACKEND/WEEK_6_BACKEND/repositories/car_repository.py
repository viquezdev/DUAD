from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.car import Car
from models.user import User


class CarRepository:
    def __init__(self,session:Session):
        self.db=session

    
    def create(self,make,model,year,user_id=None):

        user=None
        if user_id is not None:
            user=self.db.get(User,user_id)
            if not user:
                print(f"Error: User with id {user_id} not found")
                return None

        car=Car(
                make=make,
                model=model,
                year=year,
                user_id=user_id
            )  
        
        try: 
            self.db.add(car)
            self.db.commit()
            self.db.refresh(car)
            return car
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error creating car : {e}")
            return None

    

    def get_all(self):
        try:
            stmt=select(Car)
            cars= self.db.execute(stmt).scalars().all()
            return [car.to_dict() for car in cars]
        except SQLAlchemyError as e:
            print(f"Error fetching cars: {e}")
            return []

    
    
    def get_by_id(self,car_id):
        
        try:
            stmt=select(Car).where(Car.id==car_id)
            car=self.db.execute(stmt).scalar_one_or_none()
            return car.to_dict()
        except SQLAlchemyError as e:
            print(f"Error fetching car by id {car_id}: {e}")
            return None
            
            
    def update(self,car_id,make=None,model=None,year=None):
        
        try:
            car=self.db.query(Car).filter_by(id=car_id).first()
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

            self.db.commit()
            self.db.refresh(car)
            return car

        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error updating car : {e}")
            return None
    
    

    def delete(self, car_id):
        
        try:
            car = self.db.get(Car, car_id)
            if not car:
                return None
            self.db.delete(car)
            self.db.commit()
            return car
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error deleting car : {e}")
            return None


    def assign_to_user(self,car_id,user_id):
        

        try:
            car=self.db.get(Car,car_id)
            if not car:
                print(f"Car {car_id} not found")
                return None
            user=self.db.get(User,user_id)
            if not user:
                print(f"User {user_id} not found")
                return None
            car.user_id=user.id
            self.db.commit()
            self.db.refresh(car)
            return car.to_dict()

        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error assigning car to user: {e}")
            return None
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
        if not all([make, model,year]):
            print("Error: missing fields")
            return None
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
            return self.db.query(Car).all()
        except SQLAlchemyError as e:
            print(f"Error fetching cars: {e}")
            return []

    
    
    def get_by_id(self,car_id):
        
        try:
            return self.db.get(Car,car_id)
        except SQLAlchemyError as e:
            print(f"Error fetching car by id {car_id}: {e}")
            return None
            

    def update(self,car_id,**kwargs):
        car=self.get_by_id(car_id)

        if not car:
            return None
        try:
            for key,value in kwargs.items():
                if key=="id":
                    print(f"'{key}' cannot be updated")
                    continue
                
                if key=="user_id" and value is not None:  
                    if not self.db.get(User,value):
                            print(f"user_id '{value}' not found.")
                            continue
                    
                if hasattr(car,key):
                    setattr(car,key,value)
                else:
                    print(f"'{key}' cannot be updated")
            self.db.commit()
            self.db.refresh(car)
            return car
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error updating car : {e}")
            return None
    

    def delete(self, car_id):
        car=self.get_by_id(car_id)
        if not car:
            return None
        try:
            self.db.delete(car)
            self.db.commit()
            return car
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error deleting car : {e}")
            return None


    def assign_to_user(self,car_id,user_id):
        car=self.get_by_id(car_id)
        if not car:
            print(f"Car {car_id} not found")
            return None
        user=self.db.get(User,user_id)
        if not user:
            print(f"User {user_id} not found")
            return None

        try:
            car.user_id=user.id
            self.db.commit()
            self.db.refresh(car)
            return car

        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error assigning car to user: {e}")
            return None
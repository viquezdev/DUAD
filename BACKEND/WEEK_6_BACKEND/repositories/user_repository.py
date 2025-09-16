
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from models.user import User
from models.car import Car
from db import SessionLocal

class UserRepository:

    @staticmethod
    def create(name,email,username,password):

        user=User(
            name=name,
            email=email,
            username=username,
            password=password
        )
        
        try:    
            with SessionLocal() as session:
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
        except IntegrityError as e:
            print("Error: username or email already exists")
            return None


    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                users=session.query(User).all()
                return [user.to_dict() for user in users]
        except SQLAlchemyError as e:
            print(f"Error fetching users: {e}")
            return []


    @staticmethod
    def get_by_id(user_id):   
        try:
            with SessionLocal() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if user:
                    return user.to_dict()
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching user by id {user_id}: {e}")
            return None
            

    @staticmethod
    def update(user_id,name=None,email=None,username=None,password=None):
        
        try:
            with SessionLocal() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                
                fields = {
                "name": name,
                "email": email,
                "username": username,
                "password": password,
                }
                
                for attr, value in fields.items():
                    if value is not None:
                        setattr(user, attr, value)
                session.commit()
                session.refresh(user)
                return user
    
        except IntegrityError as e:
            print("Error: username or email already exists")
            return None

        except SQLAlchemyError as e:
            print(f"Error updating user : {e}")
            return None
    

    @staticmethod
    def delete(user_id):
        
        try:
            with SessionLocal() as session: 
                user = session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                session.delete(user)
                session.commit()
                return user
        except SQLAlchemyError as e:
            print(f"Error deleting user : {e}")
            return None


    @staticmethod
    def get_users_with_multiple_cars():
        try:
            with SessionLocal() as session:
                users=session.query(User).join(Car,Car.user_id==User.id).group_by(User.id).having(func.count(Car.id)>1)
                return [user.to_dict() for user in users]
        except SQLAlchemyError as e:
            print(f"Error fetching users: {e}")
            return []
        
    
    @staticmethod
    def get_cars_addresses_from_user(user_id):
        try:
            with SessionLocal() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                return {"cars":[car.to_dict() for car in user.cars],"addresses":[address.to_dict() for address in user.addresses]}
        except SQLAlchemyError as e:
            print(f"Error fetching users: {e}")
            return []

    


from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func
from models.user import User
from db import SessionLocal


class UserRepository:
    def __init__(self,session_factory=SessionLocal,password_manager=None):
        self.session_factory=session_factory
        self.password_manager=password_manager


    def create(self,username,password,role):
        
        hashed_pw=self.password_manager.hash_password(password)
        user=User(
            username=username,
            password=hashed_pw,
            role=role
        )
        
        try:    
            with self.session_factory() as session:
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
        except IntegrityError as e:
            print("Error: username already exists")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                users=session.query(User).all()
                return users
        except SQLAlchemyError as e:
            print(f"Error fetching users: {e}")
            return []


    def get_by_id(self,user_id):   
        try:
            with self.session_factory() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if user:
                    return user
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching user by id {user_id}: {e}")
            return None
        
    def get_by_username(self,username):
        try:
            with self.session_factory() as session:
                user=session.query(User).filter_by(username=username).one_or_none()
                if user:
                    return user
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching user by username {username}: {e}")
            return None

        
    def update(self,user_id,username=None,role=None):
        
        try:
            with self.session_factory() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                
                fields = {
                "username": username,
                "role":role
                }
                
                for attr, value in fields.items():
                    if value is not None:
                        setattr(user, attr, value)
                session.commit()
                session.refresh(user)
                return user
    
        except IntegrityError as e:
            print("Error: username  already exists")
            return None

        except SQLAlchemyError as e:
            print(f"Error updating user : {e}")
            return None
    

    def delete(self,user_id):
        
        try:
            with self.session_factory() as session: 
                user = session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                session.delete(user)
                session.commit()
                return user
        except SQLAlchemyError as e:
            print(f"Error deleting user : {e}")
            return None


    # @staticmethod
    # def get_users_with_multiple_cars():
    #     try:
    #         with SessionLocal() as session:
    #             users=session.query(User).join(Car,Car.user_id==User.id).group_by(User.id).having(func.count(Car.id)>1)
    #             return [user.to_dict() for user in users]
    #     except SQLAlchemyError as e:
    #         print(f"Error fetching users: {e}")
    #         return []
        
    
    # @staticmethod
    # def get_cars_addresses_from_user(user_id):
    #     try:
    #         with SessionLocal() as session:
    #             user=session.query(User).filter_by(id=user_id).one_or_none()
    #             if not user:
    #                 return None
    #             return {"cars":[car.to_dict() for car in user.cars],"addresses":[address.to_dict() for address in user.addresses]}
    #     except SQLAlchemyError as e:
    #         print(f"Error fetching users: {e}")
    #         return []

    

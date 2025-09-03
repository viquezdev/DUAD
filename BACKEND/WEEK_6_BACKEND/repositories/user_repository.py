from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.user import User


class UserRepository:
    def __init__(self,session:Session):
        self.db=session

    
    def create(self,name,email,username,password):
        
        user=User(
            name=name,
            email=email,
            username=username,
            password=password
        )
        
        try:    
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user
        except IntegrityError as e:
            self.db.rollback()
            print("Error: username or email already exists")
            return None

    
    def get_all(self):
        try:
            stmt=select(User)
            users= self.db.execute(stmt).scalars().all()
            return [user.to_dict() for user in users]
        except SQLAlchemyError as e:
            print(f"Error fetching users: {e}")
            return []

    
    def get_by_id(self,user_id):   
        try:
            stmt=select(User).where(User.id==user_id)
            user=self.db.execute(stmt).scalar_one_or_none()
            return user.to_dict()
        except SQLAlchemyError as e:
            print(f"Error fetching user by id {user_id}: {e}")
            return None
            

    def update(self,user_id,name=None,email=None,username=None,password=None):
        
        try:
            user=self.db.query(User).filter_by(id=user_id).first()
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

            self.db.commit()
            self.db.refresh(user)
            return user
    
        except IntegrityError as e:
            self.db.rollback()
            print("Error: username or email already exists")
            return None

        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error updating user : {e}")
            return None
    

    def delete(self, user_id):
        
        try:
            user = self.db.get(User, user_id)
            if not user:
                return None
            self.db.delete(user)
            self.db.commit()
            return user
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error deleting user : {e}")
            return None

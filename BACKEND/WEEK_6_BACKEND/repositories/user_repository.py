from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.user import User


class UserRepository:
    def __init__(self,session:Session):
        self.db=session

    
    def create(self,name,email,username,password):
        if not all([name, email,username,password]):
            print("Error: missing fields")
            return None
        
        
        
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
            return self.db.execute(stmt).scalars().all()
        except SQLAlchemyError as e:
            print(f"Error fetching users: {e}")
            return []

    
    
    def get_by_id(self,user_id):
        stmt=select(User).where(User.id==user_id)
        try:
            return self.db.execute(stmt).scalar_one_or_none()
        except SQLAlchemyError as e:
            print(f"Error fetching user by id {user_id}: {e}")
            return None
            

    def update(self,user_id,**kwargs):
        user=self.get_by_id(user_id)
        if not user:
            return None
        try:
            for key,value in kwargs.items():
                if hasattr(user,key) and key!="id":
                    setattr(user,key,value)
                else:
                    print(f"'{key}' cannot be updated")
            self.db.commit()
            self.db.refresh(user)
            return user
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error updating user : {e}")
            return None
    

    def delete(self, user_id):
        user=self.get_by_id(user_id)
        if not user:
            return None
        try:
            self.db.delete(user)
            self.db.commit()
            return user
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error deleting user : {e}")
            return None

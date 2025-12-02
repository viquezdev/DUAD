

from sqlalchemy.exc import SQLAlchemyError
from models.user import User
from db.db import SessionLocal
from db.db import SessionLocal


class UserRepository:
    def __init__(self,session_factory=SessionLocal,password_manager=None):
        self.session_factory=session_factory
        self.password_manager=password_manager

    def create(self, username,password,email,is_admin,created_at,updated_at):
        try:
            hashed_pw=self.password_manager.hash_password(password)
            user=User(
                username=username,
                password=hashed_pw,
                email=email,
                is_admin=is_admin,
                created_at=created_at,
                updated_at=updated_at
            )
            with self.session_factory() as session:
                session.add(user)
                session.commit()
                session.refresh(user)
                return user
        except SQLAlchemyError as e:
            print(f"Error creating user:{e}")
            return None


    def update(self,id,username=None,email=None,is_admin=None,created_at=None,updated_at=None):
        try:
            with self.session_factory() as session:
                found_user=session.query(User).filter_by(id=id).one_or_none()
                if not found_user:
                    return None
                fields={
                    "username":username,
                    "email":email,
                    "is_admin":is_admin,
                    "created_at":created_at,
                    "updated_at":updated_at
                }
                for attr,value in fields.items():
                    if value is not None:
                        setattr(found_user,attr,value)
                session.commit()
                session.refresh(found_user)
                return found_user
        except SQLAlchemyError as e:
            print(f"Error updating user: {e}")
            return None


    def delete(self,user_id):
        try:
            with self.session_factory() as session:
                found_user=session.query(User).filter_by(id=user_id).one_or_none()
                if not found_user:
                    return None
                session.delete(found_user)
                session.commit()
                return found_user
        except SQLAlchemyError as e:
            print(f"Error deleting user: {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                found_users=session.query(User).all()
                return found_users            
        except SQLAlchemyError as e:
            print(f"Error fetching users: {e}")
            return []


    def get_by_id(self,user_id):
        try:
            with self.session_factory() as session:
                found_user=session.query(User).filter_by(id=user_id).one_or_none()
                if not found_user:
                    return None
                return found_user
        except SQLAlchemyError as e:
            print(f"Error fetching user by id {user_id}: {e}")
            return None
        

    def get_by_username(self,username):
        try:
            with self.session_factory() as session:
                found_user=session.query(User).filter_by(username=username).one_or_none()
                if not found_user:
                    return None
                return found_user
        except SQLAlchemyError as e:
            print(f"Error fetching user by username {username}: {e}")
            return None


    def get_by_email(self,email):
        try:
            with self.session_factory() as session:
                found_user=session.query(User).filter_by(email=email).one_or_none()
                if not found_user:
                    return None
                return found_user
        except SQLAlchemyError as e:
            print(f"Error fetching user by email {email}: {e}")
            return None


    def count(self):
        with self.session_factory() as session:
            return session.query(User).count()
        
    
    
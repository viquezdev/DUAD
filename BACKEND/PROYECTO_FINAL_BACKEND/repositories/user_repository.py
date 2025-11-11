from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models.user import User
from db import SessionLocal

class UserRepository:
    def __init__(self,session_factory=SessionLocal,password_manager=None):
        self.session_factory=session_factory
        self.password_manager=password_manager

        def create(self, username,email,is_admin,created_at,updated_at):
            pass

        def update(self,id,username=None,email=None,is_admin=None,created_at=None,updated_at=None):
            pass

        def delete(self):
            pass

        def get_all(self):
            pass

        def get_by_id(self,user_id):
            pass

        def get_by_username(self,username):
            pass

        def get_by_email(self,email):
            pass
from sqlalchemy.exc import SQLAlchemyError
from models.user import User
from db.db import SessionLocal
from models.login_history import LoginHistory


class LoginHistoryRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory


    def create(self, user_id,login_at,ip_address,is_successful):
        
        try:
            with self.session_factory() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                
                login_history=LoginHistory(
                        user_id=user_id,
                        login_at=login_at,
                        ip_address=ip_address,
                        is_successful=is_successful
                    )  
            
                session.add(login_history)
                session.commit()
                session.refresh(login_history)
                return login_history
        except SQLAlchemyError as e:
            print(f"Error creating login_history : {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                login_history= session.query(LoginHistory).all()
                return login_history
        except SQLAlchemyError as e:
            print(f"Error fetching login_history: {e}")
            return []
        

    def get_by_id(self,user_id):   
        try:
            with self.session_factory() as session:
                login_history=session.query(LoginHistory).filter_by(user_id=user_id).all()
                if login_history:
                    return login_history
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching login history {user_id}: {e}")
            return None
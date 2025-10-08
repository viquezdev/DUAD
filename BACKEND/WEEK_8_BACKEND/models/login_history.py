from sqlalchemy import Column,Integer,String,ForeignKey,DateTime,Boolean
from sqlalchemy.orm import relationship
from .base import Base


class LoginHistory(Base):
    __tablename__="login_history"

    id=Column(Integer,primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    login_at=Column(DateTime,nullable=False)
    ip_address=Column(String(45),nullable=True)
    is_successful=Column(Boolean,nullable=False)

    user = relationship("User", back_populates="login_history")

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "login_at": self.login_at.isoformat(),
            "ip_address": self.ip_address,
            "is_successful": self.is_successful
        }
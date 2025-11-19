from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from models.shopping_cart import ShoppingCart
from models.user import User
from db.db import SessionLocal

class ShoppingCartRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory


    def create(self,user_id,status,created_at):
        try:
            with self.session_factory() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    print(f"User with id {user_id} not found.")
                    return None                   
                shopping_cart=ShoppingCart(
                    user_id=user_id,
                    status=status,
                    created_at=created_at
                    )
                session.add(shopping_cart)
                session.commit()
                session.refresh(shopping_cart)
                return shopping_cart
        except SQLAlchemyError as e:
            print(f"Error creating shopping cart: {e}")
            return None
        

    def update(self,id,user_id=None,status=None,created_at=None):
        try:
            with self.session_factory() as session:
                shopping_cart=session.query(ShoppingCart).filter_by(id=id).one_or_none()
                if not shopping_cart:
                    print(f"Shopping cart with id {id} not found.")
                    return None
                if user_id:
                    user=session.query(User).filter_by(id=user_id).one_or_none()
                    if not user:
                        print(f"User with id {user_id} not found.")
                        return None                   
                fields={
                    "user_id":user_id,
                    "status":status,
                    "created_at":created_at
                }
                for attr,value in fields.items():
                    if value is not None:
                        setattr(shopping_cart,attr,value)                   
                session.commit()
                session.refresh(shopping_cart)
                return shopping_cart
        except SQLAlchemyError as e:
            print(f"Error updating shopping cart: {e}")
            return None


    def delete(self,id):
        try:
            with self.session_factory() as session:
                shopping_cart=session.query(ShoppingCart).filter_by(id=id).one_or_none()
                if not shopping_cart:
                    print(f"Shopping Cart with id {id} not found.")
                    return None
                session.delete(shopping_cart)
                session.commit()
                return shopping_cart
        except SQLAlchemyError as e:
            print(f"Error deleting shopping cart: {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                shopping_carts=session.query(ShoppingCart).all()
                return shopping_carts
        except SQLAlchemyError as e:
            print(f"Error fetching shopping carts: {e}")
            return []


    def get_by_user_id(self,user_id):
        try:
            with self.session_factory() as session:
                shopping_carts=session.query(ShoppingCart).filter_by(user_id=user_id).all()
                return shopping_carts
        except SQLAlchemyError as e:
            print(f"Error fetching shopping cart: {e}")
            return []


    def get_by_status(self,status):
        try:
            with self.session_factory() as session:
                shopping_carts=session.query(ShoppingCart).filter_by(status=status).all()
                return shopping_carts
        except SQLAlchemyError as e:
            print(f"Error fetching shopping cart: {e}")
            return []




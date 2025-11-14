
from sqlalchemy.exc import SQLAlchemyError
from models.shopping_cart_product import ShoppingCartProduct
from models.shopping_cart import ShoppingCart
from models.product import Product
from db import SessionLocal

class ShoppingCartProductRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory

        def create(self,shopping_cart_id,product_id,quantity,subtotal):
            try:
                with self.session_factory() as session:
                    found_shopping_cart=session.query(ShoppingCart).filter_by(id=shopping_cart_id).one_or_none()
                    if not found_shopping_cart:
                        print(f"Shopping cart with id {shopping_cart_id} not found")
                        return None
                    found_product=session.query(Product).filter_by(id=product_id).one_or_none()
                    if not found_product:
                        print(f"Product with id {product_id} not found")
                        return None
                    shopping_cart_product=ShoppingCartProduct(
                        shopping_cart_id=shopping_cart_id,
                        product_id=product_id,
                        quantity=quantity,
                        subtotal=subtotal
                        )
                    session.add(shopping_cart_product)
                    session.commit()
                    session.refresh(shopping_cart_product)
                    return shopping_cart_product
            except SQLAlchemyError as e:
                print(f"Error creating shopping cart product: {e}")

        def update(self,id,shopping_cart_id=None,product_id=None,quantity=None,subtotal=None):
            try:
                with self.session.factory() as session:
                    found_shopping_cart_product=session.query(ShoppingCartProduct).filter_by(id=id).one_or_none()
                    if not found_shopping_cart_product:
                        print(f"Shopping cart product with id {id} not found.")
                        return None
                    if shopping_cart_id:
                        found_shopping_cart=session.query(ShoppingCart).filter_by(id=shopping_cart_id).one_or_none()
                        if not found_shopping_cart:
                            print(f"Shopping cart with id {shopping_cart_id} not found.")
                            return None
                    if product_id:
                        found_product=session.query(Product).filter_by(id=product_id).one_or_none()
                        if not found_product:
                            print(f"Product with id {product_id} not found.")
                            return None
                    fields={
                        "shopping_cart_id":shopping_cart_id,
                        "product_id":product_id,
                        "quantity":quantity,
                        "subtotal":subtotal
                    }
                    for attr,value in fields.items():
                        if value is not None:
                            setattr(found_shopping_cart_product,attr,value)
                    session.commit()
                    session.refresh(found_shopping_cart_product)
            except SQLAlchemyError as e:
                print(f"Error updating shopping cart product: {e}")

        def delete(self,id):
            try:
                with self.session_factory() as session:
                    found_shopping_cart_product=session.query(ShoppingCartProduct).filter_by(id=id).one_or_none()
                    if not found_shopping_cart_product:
                        print(f"Shopping cart product with id {id} not found.")
                        return None
                    session.delete(found_shopping_cart_product)
                    session.commit()
                    return found_shopping_cart_product
            except SQLAlchemyError as e:
                print(f"Error deleting return: {e}")

        def get_all(self):
            try:
                with self.session_factory() as session:
                    shopping_cart_products=session.query(ShoppingCartProductRepository).all()
                    return shopping_cart_products
            except SQLAlchemyError as e:
                print(f"Error fetching shopping cart products: {e}")
                return []

        def get_by_shopping_cart_id(self,shopping_cart_id):
            try:
                with self.session_factory() as session:
                    shopping_cart_products=session.query(ShoppingCartProduct).filter_by(shopping_cart_id=shopping_cart_id).all()
                    return shopping_cart_products
            except SQLAlchemyError as e:
                print(f"Error fetching shopping cart products: {e}")
                return []

        def get_by_product_id(self,product_id):
            try:
                with self.session_factory() as session:
                    shopping_cart_products=session.query(ShoppingCartProduct).filter_by(product_id=product_id).all()
                    return shopping_cart_products
            except SQLAlchemyError as e:
                print(f"Error fetching shopping cart products: {e}")
                return []




        
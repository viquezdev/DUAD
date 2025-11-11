from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base
from models import user,product,shopping_cart,shopping_cart_product,invoice,returns



engine=create_engine("postgresql+psycopg2://postgres:VKVLLNTL2U@localhost:5432/postgres",echo=True)
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
Base.metadata.create_all(bind=engine)

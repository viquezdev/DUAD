from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import select
from models.address import Address
from models.user import User


class AddressRepository:
    def __init__(self,session:Session):
        self.db=session

    
    def create(self,street,city,postal_code=None,country=None,user_id=None):
        if not all([street, city, user_id]):
            print("Error: missing fields")
            return None
        
        
        user=self.db.get(User,user_id)
        if not user:
            print(f"Error: User with id {user_id} not found")
            return None
        
        address=Address(
                street=street,
                city=city,
                postal_code=postal_code,
                country=country,
                user_id=user_id
            )  
        
        try: 
            self.db.add(address)
            self.db.commit()
            self.db.refresh(address)
            return address
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error creating address : {e}")
            return None

    

    def get_all(self):
        try:
            return self.db.query(Address).all()
        except SQLAlchemyError as e:
            print(f"Error fetching addresses: {e}")
            return []

    
    
    def get_by_id(self,address_id):
        
        try:
            return self.db.get(Address,address_id)
        except SQLAlchemyError as e:
            print(f"Error fetching address by id {address_id}: {e}")
            return None
            

    def update(self,address_id,**kwargs):
        address=self.get_by_id(address_id)
        if not address:
            print(f"Address with id {address_id} not found")
            return None
        try:
            for key,value in kwargs.items():
                if key=="id":
                    print(f"'{key}' cannot be updated")
                    continue
                
                if key=="user_id" and value is not None:  
                    if not self.db.get(User,value):
                        print(f"user_id '{value}' not found.")
                        continue
                
                if hasattr(address,key):
                    setattr(address,key,value)
                else:
                    print(f"'{key}' cannot be updated")
            self.db.commit()
            self.db.refresh(address)
            return address
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error updating address : {e}")
            return None
    

    def delete(self, address_id):
        address=self.get_by_id(address_id)
        if not address:
            print(f"Address with id {address_id} not found")
            return None
        try:
            self.db.delete(address)
            self.db.commit()
            return address
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error deleting address : {e}")
            return None


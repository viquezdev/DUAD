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
            stmt=select(Address)
            addresses= self.db.execute(stmt).scalars().all()
            return [address.to_dict() for address in addresses]
        except SQLAlchemyError as e:
            print(f"Error fetching addresses: {e}")
            return []

    
    def get_by_id(self,address_id):
        
        try:
            stmt=select(Address).where(Address.id==address_id)
            address=self.db.execute(stmt).scalar_one_or_none()
            return address.to_dict()
        except SQLAlchemyError as e:
            print(f"Error fetching address by id {address_id}: {e}")
            return None
        
    
    def update(self,address_id,street=None,city=None,postal_code=None,country=None):
        
        try:
            address=self.db.query(Address).filter_by(id=address_id).first()
            if not address:
                return None
            
            fields = {
            "street": street,
            "city": city,
            "postal_code": postal_code,
            "country":country
            }
            for attr, value in fields.items():
                if value is not None:
                    setattr(address, attr, value)

            self.db.commit()
            self.db.refresh(address)
            return address

        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error updating address : {e}")
            return None
            
    
    def delete(self, address_id):
        
        try:
            address = self.db.get(Address, address_id)
            if not address:
                return None
            self.db.delete(address)
            self.db.commit()
            return address
        except SQLAlchemyError as e:
            self.db.rollback()
            print(f"Error deleting address : {e}")
            return None


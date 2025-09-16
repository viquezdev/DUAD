
from sqlalchemy.exc import SQLAlchemyError
from models.address import Address
from models.user import User
from db import SessionLocal

class AddressRepository:
    
    @staticmethod
    def create(street,city,postal_code=None,country=None,user_id=None):
        
        try:
            with SessionLocal() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                
                address=Address(
                        street=street,
                        city=city,
                        postal_code=postal_code,
                        country=country,
                        user_id=user_id
                    )  
            
                session.add(address)
                session.commit()
                session.refresh(address)
                return address
        except SQLAlchemyError as e:
            print(f"Error creating address : {e}")
            return None


    @staticmethod
    def get_all():
        try:
            with SessionLocal() as session:
                addresses= session.query(Address).all()
                return [address.to_dict() for address in addresses]
        except SQLAlchemyError as e:
            print(f"Error fetching addresses: {e}")
            return []


    @staticmethod
    def get_by_id(address_id):
        
        try:
            with SessionLocal() as session:
                address=session.query(Address).filter_by(id=address_id).one_or_none()
                if address:
                    return address.to_dict()
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching address by id {address_id}: {e}")
            return None
        

    @staticmethod
    def update(address_id,street=None,city=None,postal_code=None,country=None):
        
        try:
            with SessionLocal() as session:    
                address=session.query(Address).filter_by(id=address_id).one_or_none()
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
                session.commit()
                session.refresh(address)
                return address

        except SQLAlchemyError as e:
            print(f"Error updating address : {e}")
            return None
            
    
    @staticmethod
    def delete(address_id):
        
        try:
            with SessionLocal() as session:    
                address =session.query(Address).filter_by(id=address_id).one_or_none() 
                if not address:
                    return None
                session.delete(address)
                session.commit()
                return address
        except SQLAlchemyError as e:
            print(f"Error deleting address : {e}")
            return None


    @staticmethod
    def get_addresses_with_street():
        try:
            with SessionLocal() as session:
                addresses= session.query(Address).filter(Address.street.ilike("%street%")).all()
                return [address.to_dict() for address in addresses]
        except SQLAlchemyError as e:
            print(f"Error fetching addresses: {e}")
            return []



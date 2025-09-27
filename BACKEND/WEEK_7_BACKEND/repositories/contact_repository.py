from sqlalchemy.exc import SQLAlchemyError
from models.user import User
from db import SessionLocal
from models.contact import Contact


class ContactRepository:
    def __init__(self,session_factory=SessionLocal):
        self.session_factory=session_factory


    def create(self, user_id,name,phone,email):
        
        try:
            with self.session_factory() as session:
                user=session.query(User).filter_by(id=user_id).one_or_none()
                if not user:
                    return None
                
                contact=Contact(
                        user_id=user_id,
                        name=name,
                        phone=phone,
                        email=email
                    )  
            
                session.add(contact)
                session.commit()
                session.refresh(contact)
                return contact
        except SQLAlchemyError as e:
            print(f"Error creating contact : {e}")
            return None


    def get_all(self):
        try:
            with self.session_factory() as session:
                contacts= session.query(Contact).all()
                return contacts
        except SQLAlchemyError as e:
            print(f"Error fetching contacts: {e}")
            return []


    def get_by_id(self,contact_id):
        
        try:
            with self.session_factory() as session:
                contact=session.query(Contact).filter_by(id=contact_id).one_or_none()
                if contact:
                    return contact
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching contact by id {contact_id}: {e}")
            return None
        
    def get_by_user(self,user_id):
        
        try:
            with self.session_factory() as session:
                contacts=session.query(Contact).filter_by(user_id=user_id).all()
                if contacts:
                    return contacts
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching contacts: {e}")
            return None
        
    def get_user_id(self,contact_id):
        
        try:
            with self.session_factory() as session:
                contact=session.query(Contact).filter_by(id=contact_id).one_or_none()
                if contact:
                    return contact.user_id
                return None
        except SQLAlchemyError as e:
            print(f"Error fetching contact by id {contact_id}: {e}")
            return None
        

    def update(self,contact_id,name,phone,email):
        
        try:
            with self.session_factory() as session:    
                contact=session.query(Contact).filter_by(id=contact_id).one_or_none()
                if not contact:
                    return None
                
                fields = {
                "name": name,
                "phone": phone,
                "email": email
                }

                for attr, value in fields.items():
                    if value is not None:
                        setattr(contact, attr, value)
                session.commit()
                session.refresh(contact)
                return contact

        except SQLAlchemyError as e:
            print(f"Error updating invoice : {e}")
            return None
            
    
    def delete(self,contact_id):
        
        try:
            with self.session_factory() as session:    
                contact =session.query(Contact).filter_by(id=contact_id).one_or_none() 
                if not contact:
                    return None
                session.delete(contact)
                session.commit()
                return contact
        except SQLAlchemyError as e:
            print(f"Error deleting invoice : {e}")
            return None


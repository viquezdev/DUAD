
from repositories.car_repository import CarRepository
from repositories.user_repository import UserRepository
from repositories.address_repository import AddressRepository
from sqlalchemy.orm import Session

from faker import Faker
import random


def seed_database(session):
    try:
        
        fake=Faker()
        users_repo=UserRepository(session)
        cars_repo=CarRepository(session)
        addresses_repo=AddressRepository(session)
    
        for _ in range(20):
            name = fake.name()
            email = fake.email()
            username = fake.user_name()
            password = fake.password(length=8) 
            users_repo.create(name,email,username,password)

        for _ in range(20):
            make = fake.company()                
            model = random.choice(["Civic", "Corolla", "Mustang", "Model S", "Camry"]) 
            year = random.randint(2000, 2025)  
            user_id = random.choice([None,random.randint(1, 20)]) 
            cars_repo.create(make,model,year,user_id) 

        

        for _ in range(20):
            street=fake.street_address()
            city=fake.city()
            postal_code=fake.postalcode()
            country=fake.country()
            user_id=random.randint(1,20)
            addresses_repo.create(street,city,postal_code,country,user_id)

        session.commit()
        print("Database seeded successfully")

    except Exception as ex:
        session.rollback()
        print(f"DB error: {ex}")  


if __name__ == "__main__":
    seed_database()
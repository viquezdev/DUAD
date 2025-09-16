
from repositories.car_repository import CarRepository
from repositories.user_repository import UserRepository
from repositories.address_repository import AddressRepository
from faker import Faker
import random


def seed_database():
    try:
        
        fake=Faker()
    
        for _ in range(20):
            name = fake.name()
            email = fake.email()
            username = fake.user_name()
            password = fake.password(length=8) 
            UserRepository.create(name,email,username,password)

        for _ in range(20):
            make = fake.company()                
            model = random.choice(["Civic", "Corolla", "Mustang", "Model S", "Camry"]) 
            year = random.randint(2000, 2025)  
            user_id = random.choice([None,random.randint(1, 20)]) 
            CarRepository.create(make,model,year,user_id) 

        

        for _ in range(20):
            street=fake.street_address()
            city=fake.city()
            postal_code=fake.postalcode()
            country=fake.country()
            user_id=random.randint(1,20)
            AddressRepository.create(street,city,postal_code,country,user_id)
        
        
        print("Database seeded successfully")

    except Exception as ex:
        
        print(f"DB error: {ex}")  
    
        

if __name__ == "__main__":
    seed_database()
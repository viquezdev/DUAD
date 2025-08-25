from app.db.pg_manager import PgManager
from app.repositories.car_repository import CarRepository
from app.repositories.user_repository import UserRepository
from app.repositories.car_rental_repository import CarRentalRepository

from faker import Faker
import random


def seed_database():
    try:
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        
        fake=Faker()
        users_repo=UserRepository(db_manager)
        cars_repo=CarRepository(db_manager)
        car_rentals_repo=CarRentalRepository(db_manager)
    
        for _ in range(200):
            name = fake.name()
            email = fake.email()
            username = fake.user_name()
            password = fake.password(length=8) 
            birth_date = fake.date_of_birth(minimum_age=18, maximum_age=70)
            account_status = random.choice(["active", "inactive", "suspended"])
            users_repo.create(name,email,username,password,birth_date,account_status)

        for _ in range(100):
            make = fake.company()                
            model = random.choice(["Civic", "Corolla", "Mustang", "Model S", "Camry"]) 
            manufacture_year = random.randint(2000, 2025)  
            car_status = random.choice(["available", "rented", "maintenance","sold","unavailable"]) 
            cars_repo.create(make,model,manufacture_year,car_status) 

        user_ids = [row[0] for row in db_manager.execute_query("SELECT id FROM lyfter_car_rental.users;")]
        car_ids = [row[0] for row in db_manager.execute_query("SELECT id FROM lyfter_car_rental.cars;")]

        for _ in range(random.randint(50, 150)):
            user_id=random.choice(user_ids)
            car_id=random.choice(car_ids)
            rental_date=fake.date_this_year()
            rental_status=random.choice(["active", "completed", "cancelled"])
            car_rentals_repo.create(user_id,car_id,rental_date,rental_status)

        db_manager.close_connection()
        print("Database seeded successfully")

    except Exception as ex:
        print(f"DB error: {ex}")  


if __name__ == "__main__":
    seed_database()
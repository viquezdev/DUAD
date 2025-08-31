from app.db.pg_manager import PgManager
from app.repositories.car_repository import CarRepository
from app.repositories.user_repository import UserRepository
from app.repositories.car_rental_repository import CarRentalRepository
from datetime import datetime

import csv
import os




def export_data_to_csv():
    try:
        db_manager = PgManager(
        db_name="postgres",
        user="postgres",
        password="VKVLLNTL2U",
        host="localhost"
        )
        
        users_repo=UserRepository(db_manager)
        cars_repo=CarRepository(db_manager)
        car_rentals_repo=CarRentalRepository(db_manager)

        users_data=users_repo.get_all()
        cars_data=cars_repo.get_all()
        car_rentals_data=car_rentals_repo.get_all()
        
        folder_name="db_backups"
        if not os.path.exists(folder_name):
            os.makedirs(folder_name)
            print(f"The folder '{folder_name}' was created")
        else:
            print(f"The folder '{folder_name}' already exists")

        today=datetime.now().strftime("%Y-%m-%d")
        file_users = os.path.join(folder_name, f"backup_{today}_users.csv")
        file_cars = os.path.join(folder_name, f"backup_{today}_cars.csv")
        file_rentals = os.path.join(folder_name, f"backup_{today}_car_rentals.csv")

        
        user_headers=["id","name","email","username","password","birth_date","account_status"]
        car_headers=["id","make","model","manufacture_year","car_status"]
        car_rentals_headers=["id","user_id","car_id","rental_date","rental_status"]
        
        with open(file_users, 'w',newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file,fieldnames= user_headers,delimiter=',')
            writer.writeheader()
            writer.writerows(users_data)

        with open(file_cars, 'w',newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file,fieldnames= car_headers,delimiter=',')
            writer.writeheader()
            writer.writerows(cars_data)
        
        with open(file_rentals, 'w',newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file,fieldnames= car_rentals_headers,delimiter=',')
            writer.writeheader()
            writer.writerows(car_rentals_data)

        print("Backup exported successfully")
        db_manager.close_connection()
    except Exception as ex:
        print(f"Backup error: {ex}")  


if __name__ == "__main__":
    export_data_to_csv()
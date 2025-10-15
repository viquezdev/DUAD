
from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from repositories.invoice_repository import InvoiceRepository
from repositories.invoice_products_repository import InvoiceProductsRepository
from repositories.contact_repository import ContactRepository
from repositories.login_history_repository import LoginHistoryRepository
from services.password_manager import PasswordManager
from faker import Faker
import random
from datetime import date


def seed_database():
    try:
        fake=Faker()
        password_manager = PasswordManager()
        user_repo = UserRepository(password_manager=password_manager)
        product_repo = ProductRepository()
        invoice_repo = InvoiceRepository()
        invoice_products_repo = InvoiceProductsRepository()
        contact_repo=ContactRepository()
        login_repo=LoginHistoryRepository()
        
        for _ in range(10):
            username = fake.user_name()
            password = fake.password(length=8)
            role=random.choice(["user","administrator"])
            user_repo.create(username,password,role)

        #user_repo.create('dakin5','dako3113','administrator')
        #user_repo.create('dakin6','dako3113','user')


        for _ in range(5):
            user_id=random.randint(1,10)
            name=fake.name()
            phone = fake.phone_number()
            email=fake.email()
            contact_repo.create(user_id,name,phone,email)

        for _ in range(5):
            user_id=random.randint(1,10)
            login_at=fake.date_time()
            ip_address = fake.ipv4()
            is_successful=fake.boolean()
            login_repo.create(user_id,login_at,ip_address,is_successful)
        
        fruits = [
            "apple", "banana", "orange", "pear", "grape", "kiwi", "mango",
            "strawberry", "watermelon", "pineapple", "cherry", "melon", "lemon", "mandarin",
            "peach", "papaya", "blueberry", "raspberry", "guava", "coconut"
        ]
        
        for name in fruits:      
            price = round(random.uniform(500, 1500), 2)
            entry_date = fake.date_between(start_date='-30d', end_date='today')
            quantity = random.randint(1,15)
            product_repo.create(name, price,entry_date,quantity) 

        for _ in range(5):
            user_id=random.randint(1,10)
            total_amount=0
            invoice_date = date.today()
            invoice_repo.create(user_id,total_amount,invoice_date)

        for _ in range(5):
            invoice_id=random.randint(1,5)
            product_id=random.randint(1,20)
            quantity = random.randint(1,5)
            product=product_repo.get_by_id(product_id)
            unit_price=product.price
            subtotal= unit_price * quantity
            invoice_products_repo.create(invoice_id,product_id,quantity,subtotal)

        invoice_repo.update_totals()
        
        
        
        print("Database seeded successfully")

    except Exception as ex:
        
        print(f"DB error: {ex}")  
    
        

if __name__ == "__main__":
    seed_database()
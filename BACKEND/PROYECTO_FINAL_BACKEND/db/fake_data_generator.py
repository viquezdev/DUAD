from repositories.user_repository import UserRepository
from repositories.product_repository import ProductRepository
from repositories.shopping_cart_repository import ShoppingCartRepository
from repositories.shopping_cart_product_repository import ShoppingCartProductRepository
from repositories.invoice_repository import InvoiceRepository
from repositories.returns_repository import ReturnsRepository
from services.password_manager import PasswordManager
from faker import Faker
import random,string
from datetime import date

def create_sku(name):
    prefix=name[:3].upper()
    digits=''.join(random.choices(string.digits,k=5))
    return f"{prefix}-{digits}"


def seed_database():
    try:
        fake=Faker()
        password_manager=PasswordManager()
        user_repo=UserRepository(password_manager=password_manager)
        product_repo=ProductRepository()
        shopping_cart_repo=ShoppingCartRepository()
        shopping_cart_product_repo=ShoppingCartProductRepository()
        invoice_repo=InvoiceRepository()
        returns_repo=ReturnsRepository()

        if user_repo.count()>0:
            print("Database is not empty. Skippinng seeding process")
            return

        user_ids=[]
        product_ids=[]
        shopping_cart_ids=[]
        invoice_ids=[]
        
        for _ in range(10):
            username=fake.user_name()
            password=fake.password(length=8)
            email=fake.email()
            is_admin=False
            created_at=date.today()
            updated_at=date.today()
            new_user=user_repo.create(username,password,email,is_admin,created_at,updated_at)
            user_ids.append(new_user.id)

        user_repo.create("dakodako","1234","dako@gmail.com",True,date.today(),date.today())

        products_names=[
            "Premium Dry Dog Food for Adult Dogs",
            "Balanced Cat Food for Neutered Cats",
            "Anti-Flea Shampoo for Dogs and Cats",
            "Long-Lasting Anti-Parasite Collar",
            "Rubber Chew Toy for Dogs",
            "Cat Scratching Post",
            "Rigid Pet Carrier for Small Animals",
            "Adjustable Harness for Medium Dogs",
            "Clumping Cat Litter",
            "Puppy Vitamins and Supplements",
            "Soft-Bristle Pet Brush",
            "Double Anti-Slip Pet Bowl",
            "Automatic Water Dispenser for Pets",
            "Pet Grooming Gloves",
            "Dental Chew Snacks for Dogs"
        ]

        product_descriptions=[
            "Nutritious formula designed to support energy and healthy digestion in adult dogs.",
            "Special recipe to maintain weight control and urinary health in sterilized cats.",
            "Gentle cleansing shampoo that eliminates fleas and leaves a fresh scent.",
            "Protects pets against fleas and ticks for up to 8 months.",
            "Durable toy that helps reduce stress and promotes dental health.",
            "Sturdy post that satisfies natural scratching instincts and protects furniture.",
            "Safe and comfortable transport solution for cats and small dogs.",
            "Secure and comfortable harness with adjustable straps for daily walks.",
            "High-absorption litter that controls odors and makes cleaning easy.",
            "Essential nutrients to support growth, immunity, and strong bones.",
            "Gentle grooming brush that keeps fur shiny and reduces shedding.",
            "Convenient dual bowl design for food and water, with non-slip base.",
            "Keeps fresh water available all day for cats and dogs.",
            "Comfortable gloves that remove loose hair while massaging your pet.",
            "Tasty treats that help clean teeth and freshen breath."
        ]

        for name,product_description in zip(products_names,product_descriptions):
            sku=create_sku(name)
            price=round(random.uniform(1500,6000),2)
            description=product_description
            quantity=random.randint(1,10)
            new_product=product_repo.create(sku,name,price,description,quantity)
            product_ids.append(new_product.id)

        for _ in range(10):
            user_id=random.choice(user_ids)
            status=random.choice(["active","empty","cancelled"])
            created_at=date.today()
            new_shopping_cart=shopping_cart_repo.create(user_id,status,created_at)
            shopping_cart_ids.append(new_shopping_cart.id)

        for cart_id in shopping_cart_ids:
            product_id=random.choice(product_ids)
            quantity=random.randint(1,5)
            subtotal=(product_repo.get_by_id(product_id).price)*quantity
            shopping_cart_product_repo.create(cart_id,product_id,quantity,subtotal)

        for _ in range(5):
            invoice_number= fake.bothify("INV-####-??")
            user_id=random.choice(user_ids)
            shopping_cart_id=random.choice(shopping_cart_ids)
            created_at=date.today()
            billing_address=fake.address()
            payment_method=random.choice(["credit_card", "debit_card", "paypal", "bank_transfer"])
            payment_status=random.choice(["pending", "completed", "failed", "cancelled"])
            total_amount=invoice_repo.calculate_total(shopping_cart_id)
            new_invoice=invoice_repo.create(invoice_number,user_id,shopping_cart_id,created_at,billing_address,payment_method,payment_status,total_amount)
            invoice_ids.append(new_invoice.id)

        for _ in range(5):
            invoice_id=random.choice(invoice_ids)
            invoice=invoice_repo.get_by_id(invoice_id)
            items=shopping_cart_product_repo.get_by_shopping_cart_id(invoice.shopping_cart_id)
            item=random.choice(items)
            product_id=item.product_id
            quantity_returned=item.quantity
            return_date=date.today()
            reason=random.choice(["defective_product","wrong_item_sent","not_as_described","expired_product"])
            processed=random.choice([False,True])
            if processed=="approved":
                product = product_repo.get_by_id(product_id)
                new_quantity = product.quantity + quantity_returned
                product_repo.update(id=product_id, quantity=new_quantity)
            returns_repo.create(invoice_id,product_id,quantity_returned,return_date,reason,processed)

        
        print("Database seeded succesfully")

    except Exception as e:
        print(f"DB error: {e}")

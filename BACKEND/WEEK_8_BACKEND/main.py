from flask import Flask
from routes.user_routes import users_bp
from routes.product_routes import products_bp
from routes.contact_routes import contacts_bp
from routes.invoice_routes import invoices_bp
from routes.invoice_products_routes import invoice_products_bp
from db.fake_data_generator import seed_database



app=Flask(__name__)

app.register_blueprint(users_bp,url_prefix="/users")
app.register_blueprint(contacts_bp,url_prefix="/contacts")
app.register_blueprint(products_bp,url_prefix="/products")
app.register_blueprint(invoices_bp,url_prefix="/invoices")
app.register_blueprint(invoice_products_bp,url_prefix="/invoice_products")


if __name__ == "__main__":
    seed_database()
    app.run(host="localhost",port=5000,debug=False)


from flask import Flask
from routes.user_routes import users_bp
from routes.car_routes import cars_bp
from routes.address_routes import addresses_bp
from db.fake_data_generator import seed_database



app=Flask(__name__)

app.register_blueprint(users_bp,url_prefix="/users")
app.register_blueprint(cars_bp,url_prefix="/cars")
app.register_blueprint(addresses_bp,url_prefix="/addresses")

if __name__ == "__main__":
    seed_database()
    app.run(host="localhost",port=5000,debug=False)
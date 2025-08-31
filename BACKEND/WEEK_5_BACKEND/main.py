from flask import Flask
from app.routes.users import users_bp
from app.routes.cars import cars_bp
from app.routes.car_rentals import car_rentals_bp


app=Flask(__name__)

app.register_blueprint(users_bp,url_prefix="/users")
app.register_blueprint(cars_bp,url_prefix="/cars")
app.register_blueprint(car_rentals_bp,url_prefix="/car_rentals")

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)
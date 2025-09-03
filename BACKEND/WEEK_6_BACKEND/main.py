from flask import Flask,g
from routes.user_routes import users_bp
from routes.car_routes import cars_bp
from routes.address_routes import addresses_bp
from db.fake_data_generator import seed_database
from db.init_db import setup


app=Flask(__name__)

SessionLocal = setup()

with SessionLocal() as session:
    seed_database(session)
    
@app.before_request
def create_session():
    g.db = SessionLocal() 

@app.teardown_request
def shutdown_session(exception=None):
    db = g.pop("db", None)
    if db is not None:
        db.close()

app.register_blueprint(users_bp,url_prefix="/users")
app.register_blueprint(cars_bp,url_prefix="/cars")
app.register_blueprint(addresses_bp,url_prefix="/addresses")

if __name__ == "__main__":
    app.run(host="localhost",port=5000,debug=True)
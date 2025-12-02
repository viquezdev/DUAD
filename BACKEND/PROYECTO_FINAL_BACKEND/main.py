from flask import Flask
from db.fake_data_generator import seed_database
from routes.user_routes import users_bp
from routes.product_routes import products_bp
from routes.shopping_cart_routes import shopping_carts_bp



app=Flask(__name__)
app.register_blueprint(users_bp,url_prefix="/users")
app.register_blueprint(products_bp,url_prefix="/products")
app.register_blueprint(shopping_carts_bp,url_prefix="/shopping_carts")

@app.route("/seed")
def seed():
    seed_database()
    return {"status":"ok"}


if __name__=="__main__":
    app.run(host="",port=5000,debug=True)
from flask import Flask
from db.fake_data_generator import seed_database
from routes.user_routes import users_bp



app=Flask(__name__)
app.register_blueprint(users_bp,url_prefix="/users")

@app.route("/seed")
def seed():
    seed_database()
    return {"status":"ok"}


if __name__=="__main__":
    app.run(host="",port=5000,debug=True)
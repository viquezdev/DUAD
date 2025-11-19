from flask import Flask
from db.fake_data_generator import seed_database
app=Flask(__name__)


@app.route("/seed")
def seed():
    seed_database()
    return {"status":"ok"}

if __name__=="__main__":
    app.run(host="",port=5000,debug=True)
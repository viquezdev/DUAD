from flask import Flask

app=Flask(__name__)


@app.route("/<id>")
def root(id):
    return {
        "name":"dani",
        "id":id
    }

if __name__=="__main__":
    app.run(host="",port=5000,debug=True)
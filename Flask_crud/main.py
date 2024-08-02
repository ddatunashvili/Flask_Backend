from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/userDB"
mongo = PyMongo(app)


@app.route("/")
def index():
    users = mongo.db.users.find()
    return render_template("index.html", users=users)


@app.route("/add_user", methods=["POST"])
def add_user():
    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")
    image = request.form.get("image")

    mongo.db.users.insert_one(
        {"name": name, "email": email, "age": age, "image": image}
    )
    return redirect(url_for("index"))


@app.route("/update_user/<user_id>", methods=["POST"])
def update_user(user_id):
    name = request.form.get("name")
    email = request.form.get("email")
    age = request.form.get("age")
    image = request.form.get("image")
    
    mongo.db.users.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": {"name": name, "email": email, "age": age, "image": image}},
    )
    return redirect(url_for("index"))


@app.route("/delete_user/<user_id>", methods=["POST"])
def delete_user(user_id):
    mongo.db.users.delete_one({"_id": ObjectId(user_id)})
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)

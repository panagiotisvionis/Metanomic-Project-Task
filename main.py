from flask import Flask, jsonify
from pymongo import MongoClient

cluster = "mongodb://localhost:27017/Car"
client = MongoClient(cluster)
db = client.Car
col = db.CarData

app = Flask(__name__)


@app.route('/', methods=["GET"])


def get_car_from_id():
    car_id = col.find_one({"_id": "QFA8685"})
    return jsonify({"car_id": car_id})



if __name__ == "__main__":
    app.run()

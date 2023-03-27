from flask import Flask, jsonify, request,render_template
# from pymongo import MongoClient
# from bson.objectid import ObjectId

app = Flask(__name__)


@app.route('/')
def create():

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
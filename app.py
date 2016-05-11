from flask import Flask, render_template as render, jsonify, request
from records import Database

db = Database('postgres://localhost/flask_riotjs_starter')
app = Flask(__name__)

@app.route("/")
def home():
    return render('home.html')

@app.route("/items.json")
def items():
    return jsonify(
        items=[row.as_dict() for row in db.query('select * from items')]
    )

@app.route("/items.json", methods=["POST"])
def add_item():
    db.query('insert into items (body) values (:body)', body=request.values.get('body'))

    return jsonify(
        item={'body': request.values.get('body')}
    )

@app.route("/items.json", methods=["DELETE"])
def delete_item():
    db.query('delete from items where body = :body', body=request.values.get('body'))

    return jsonify(
        message="Item deleted"
    )

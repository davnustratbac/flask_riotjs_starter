from flask import Flask, render_template as render, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render('home.html')

@app.route("/items.json")
def items():
    return jsonify(
        items=[
            {'body': 'hello world'},
            {'body': 'goodnight moon'}
        ]
    )

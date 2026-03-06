from flask import Flask, jsonify
from flask_cors import CORS
from .NN import run_model

app = Flask(__name__)

# this should be deletable in prod
CORS(app)

@app.route("/api/run")
def run_script():
    accuracy = run_model()

    return jsonify({
        "status": "finished",
        "accuracy": accuracy
    })
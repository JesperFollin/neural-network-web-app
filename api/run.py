from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/api/run")
def run_script():

    return jsonify({
        "message": "Hallllå ja",
    })


# for testing only
if __name__ == "__main__":
    app.run(port=8080)
# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

FASTAPI_URL = "http://127.0.0.1:8000/get-response"


@app.route("/ask-question", methods=["POST"])
def ask_question():
    user_input = request.json.get("question")
    
    fastapi_response = requests.post(FASTAPI_URL, json={"question": user_input})
    
    return jsonify(fastapi_response.json())

if __name__ == "__main__":
    app.run(port=5000, debug=True)

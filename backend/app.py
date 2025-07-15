from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route("/api/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    income = int(data["income"])
    expenses = int(data["expenses"])

    result = subprocess.run(["g++", "calc.cpp", "-o", "calc"], capture_output=True)
    output = subprocess.run(["./calc", str(income), str(expenses)], capture_output=True, text=True)

    return jsonify({ "message": output.stdout })

if __name__ == "__main__":
    app.run()


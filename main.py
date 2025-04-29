from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Jarvis is alive!"

@app.route("/jarvis", methods=["POST"])
def jarvis():
    data = request.json
    print("Received from IFTTT:", data)
    return "Action Received by Jarvis!"

if __name__ == "__main__":
    app.run(debug=True)

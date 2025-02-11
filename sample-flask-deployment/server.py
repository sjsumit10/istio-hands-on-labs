from flask import Flask
import os

app = Flask(__name__)

@app.route("/ping")
def ping():
    return f"Hello from {os.environ.get('HOSTNAME', 'Flask!')} ", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
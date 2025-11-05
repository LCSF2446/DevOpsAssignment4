from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    message = os.getenv("APP_MESSAGE", "Hello, World!")
    return render_template("home.html", message=message)

@app.route("/health")
def health():
    health_status = os.getenv("APP_HEALTH", "Healthy")
    return render_template("health.html", health_status=health_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

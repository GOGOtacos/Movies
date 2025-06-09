# main/app.py
from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    answer = request.form.get("movie")
    if answer == "夏へのトンネルさよならの出口":  # Correct answer
        return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfAD-qbgBicYXDN61Map3G7rLwAirOu9MXIC26hdFs9nGFhsA/viewform?usp=header")
    else:
        return render_template("wrong.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

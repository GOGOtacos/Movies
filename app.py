from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret")  # Flaskセッション用の秘密鍵

# ✅ パスワード（動画内に埋め込まれるもの）
CORRECT_PASSWORD = "文化祭がんばろう"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/password", methods=["GET", "POST"])
def password():
    if request.method == "POST":
        user_input = request.form.get("password", "")
        if user_input.strip() == CORRECT_PASSWORD:
            return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfAD-qbgBicYXDN61Map3G7rLwAirOu9MXIC26hdFs9nGFhsA/viewform?usp=header")
        else:
            flash("パスワードが間違っています。もう一度確認してください。")
    return render_template("password.html")

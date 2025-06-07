from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "secret")  # 必須

CORRECT_PASSWORD = "文化祭がんばろう"  # 動画に埋め込まれるパスワード

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/password", methods=["GET", "POST"])
def password():
    if request.method == "POST":
        user_input = request.form.get("password", "")
        if user_input.strip() == CORRECT_PASSWORD:
            return redirect("https://docs.google.com/forms/d/e/1FAIpQLSfAD-qbgBicYXDN61Map3G7rLwAirOu9MXIC26hdFs9nGFhsA/viewform?usp=header")  # 投票ページにリダイレクト
        else:
            flash("パスワードが間違っています。もう一度確認してください。")
    return render_template("password.html")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host="0.0.0.0", port=port)

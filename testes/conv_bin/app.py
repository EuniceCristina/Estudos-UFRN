from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)
app.secret_key = ["projetoinformatica"]

app.route("/index", methods=["GET","POST"])
def index():
    if request.methods == "POST":
        num = request.form["numero"]
        bin = []
        while num >=1:
            resto = num % 2
            bin.insert(0, resto)
            num = num // 2
    return render_template("index.html",bin=bin)

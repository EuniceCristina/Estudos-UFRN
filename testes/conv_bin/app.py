from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)
app.secret_key = ["projetoinformatica"]

app.route("/")
def index():
    return render_template("index.html")

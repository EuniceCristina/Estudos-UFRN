from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)
app.secret_key = "projetoinformatica"

@app.route("/", methods=["GET","POST"])
def index():
    numero = request.form.get("numero")
    num = 0
    bin = []
    if numero:
        num = int(numero)
    if request.method == "POST":
        
       
        while num >=1:
            resto = num % 2
            bin.insert(0, resto)
            num = num // 2
    return render_template("index.html",bin=bin)

if (__name__) == '__main__':
    app.run(debug=True)

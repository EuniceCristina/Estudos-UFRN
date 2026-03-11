from flask import Flask, render_template, redirect, request, url_for, flash

app = Flask(__name__)
app.secret_key = "projetoinformatica"

@app.route("/", methods=["GET","POST"])
def index():
    numero = request.form.get("numero")
    base = request.form.get("base")
    num = 0
    res = []
    resultado = ""
    if numero and base:
        num = int(numero)
        base = int(base)
        
    if request.method == "POST":
        
       
        while num >=1:
            resto = num % base
            res.insert(0, resto)
            
            
            num = num // base
        for i in res:
                resultado += str(i)
    return render_template("index.html",res=resultado, base=base)

if (__name__) == '__main__':
    app.run(debug=True)

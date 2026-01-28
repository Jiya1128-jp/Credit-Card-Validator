from flask import Flask, render_template, request
from luhn import check_luhn 
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        card = request.form["card"]
        result = check_luhn(card)

    return render_template("index.html", result=result)

app.run(debug=True)
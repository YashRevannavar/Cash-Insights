from flask import Flask, render_template, redirect, url_for, request
# from expenceCI import add

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("index.html")

@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/expense", methods=["POST","GET"])
def expense():
    if request.method == "POST":
        item = request.form["item"]
        amount = request.form["amount"]
        return render_template("index.html",item=item,amount=amount)
    else:
        return render_template("expense.html")

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run(debug=True)

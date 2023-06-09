from flask import Flask, render_template, redirect, url_for, request
from webfunction import get_data_from_form
from sql import insert_to_db

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    """
    Home page
    If the expense button is pressed it will redirect to the expense page
    If the report button is pressed it will redirect to the report page
    or stay on the home page
    """
    if request.method == "POST":
        if request.form["submit_button"] == "expense":
            return redirect(url_for("expense"))
        elif request.form["submit_button"] == "report":
            return redirect(url_for("report"))
        else:
            return render_template("index.html")


@app.route("/expense", methods=["POST", "GET"])
def expense():
    if request.method == "POST":
        date, category, won, item, amount = get_data_from_form()
        insert_to_db(date, category, won, item, amount)
        return render_template("expense.html", date=date)
    else:
        return render_template("expense.html")


@app.route("/report", methods=["GET", "POST"])
def report():
    return render_template("report.html")


# Extra
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"


@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))


if __name__ == "__main__":
    app.run(debug=True)

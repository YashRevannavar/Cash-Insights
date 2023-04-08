from flask import Flask, render_template, redirect, url_for, request
from webfunction import get_data_from_form
from sql import insert_to_db

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    # if request.method == "POST":
    #     return render_template("expense.html")
    # else:
    #     pass
    return render_template("index.html")


@app.route("/expense", methods=["POST","GET"])
def expense():
    if request.method == "POST":
        date, category, won, item, amount = get_data_from_form()
        insert_to_db(date, category, won, item, amount)
        return render_template("expense.html", date=date)
    else:
        return render_template("expense.html")


# @app.route("/report", method=['GET', 'POST'])
# def report():
#     return render_template("report.html")

# Extra
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

@app.route("/admin")
def admin():
    return redirect(url_for("user", name="Admin"))

if __name__ == "__main__":
    app.run(debug=True)

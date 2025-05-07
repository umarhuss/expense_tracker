from flask import Flask, render_template

# Create an instance of the Flask class
# Template folder tells flask where to look for templates
app = Flask(__name__, template_folder="app/templates", static_folder="app/static")


# Use @app to render pages it is a decorator so a function must go below
@app.route("/")
def home():
    # This goes to homepage using the render_template function
    return render_template("Homepage.html")


@app.route("/dashboard")
def dashboard():
    # This goes to the dashboard
    return render_template("Dashboard.html")


@app.route("/balance")
def balance():
    # This goes to the balance page
    return render_template("Balance.html")


@app.route("/expenses")
def expenses():
    # This goes to the expenses page
    return render_template("Expenses.html")


@app.route("/spendings")
def spendings():
    # This goes to the spending page
    return render_template("Spendings.html")


@app.route("/savings")
def savings():
    # This goes to the savings page
    return render_template("Savings.html")


if __name__ == "__main__":
    app.run(debug=True, port=5001)

from flask import Flask, redirect, render_template, request, url_for
from app import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, NumberRange, Length


# variable to hold current balance temporarily
current_balance = 0.00


# Use @app to render pages it is a decorator so a function must go below
@app.route("/")
def home():
    # This goes to homepage using the render_template function
    return render_template("Homepage.html")


@app.route("/dashboard")
def dashboard():
    # This goes to the dashboard
    return render_template("Dashboard.html")


@app.route("/balance", methods=["GET"])
def balance():
    # This goes to the balance page
    return render_template(
        "Balance.html", show_dashboard_link=True, current_balance=current_balance
    )


@app.route("/expenses")
def expenses():
    # This goes to the expenses page
    return render_template("Expenses.html", show_dashboard_link=True)


@app.route("/spendings")
def spendings():
    # This goes to the spending page
    return render_template("Spendings.html", show_dashboard_link=True)


@app.route("/savings")
def savings():
    # This goes to the savings page
    return render_template("Savings.html", show_dashboard_link=True)


# route for the add money form
@app.route("/add_money", methods=["POST"])
def add_money():
    global current_balance
    # Get information from the form
    amount = float(request.form.get("amount"))
    # Add this to the current balance
    current_balance += amount
    # Redirect to current balance page
    return redirect(url_for("balance", 0))

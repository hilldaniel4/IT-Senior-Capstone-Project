import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, flash
app = Flask(__name__)

#Connects python to MongoDB
cluster = MongoClient("mongodb+srv://ShawnTaylor:Seniorcapstone1@seniorcapstone.ksiqj.mongodb.net/GreenGrocery?retryWrites=true&w=majority")
#DB name is GreenGrocery
db = cluster["GreenGrocery"]
#Collections name is test
collection = db["test"]

#Renders Home page.
@app.route("/")
def index():
    return render_template('index.html')

#Renders Shop page.
@app.route("/shop")
def shop():
    return render_template('shop.html')

#Renders Checkout page
@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

#Renders Order Confirmation page
@app.route('/confirm')
def confirm():
    return render_template('confirm.html')

if __name__ == "__main__":
    app.run(debug=True) 
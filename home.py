from crypt import methods
import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, flash,redirect, url_for
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

#Sends user info to database
@app.route('/add_user', methods = ["GET","POST"])
def add_user():
    usr_name = request.form.get('usrName')
    usr_email = request.form.get('usrEmail')
    usr_add1 = request.form.get('usrAdd1')
    usr_add2 = request.form.get('usrAdd2')
    usr_city = request.form.get('usrCity')
    usr_state = request.form.get('usrState')
    usr_zip = request.form.get('usrZip')
    if request.method == "POST":

       print(usr_name, usr_email,usr_add1,usr_add2,usr_city,usr_state,usr_zip)
        #return request.form.get('usrName'),request.form.get('usrEmail'),request.form.get('usrAdd1'),request.form.get('usrAdd2'),request.form.get('usrCity'),request.form.get('usrState'),request.form.get('usrZip')
    

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
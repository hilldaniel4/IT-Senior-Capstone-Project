from crypt import methods
import pymongo as pym
#from pymongo import MongoClient
from flask import Flask, render_template, request, flash,redirect, url_for
#from flask_pymongo import PyMongo

app = Flask(__name__)

#Connects python to MongoDB
cluster = pym.MongoClient("mongodb+srv://test_db:Password123456@cluster0.adys6.mongodb.net/user_db?retryWrites=true&w=majority")
#DB name is GreenGrocery
db = cluster["user_db"]
#Collections name is test
collection = db["user_collection"]

#Renders Home page.
@app.route("/")
def index():
    return render_template('index.html')

#Renders Shop page.
@app.route("/shop")
def shop():
    return render_template('shop.html')

#Sends user info to database
@app.route('/add_user', methods = ["POST"])
def add_user():
    
    
    if request.method == "POST":
        items = request.form.getlist('item')
        usr_name = request.form.get('usrName')
        usr_email = request.form.get('usrEmail')
        usr_add1 = request.form.get('usrAdd1')
        usr_add2 = request.form.get('usrAdd2')
        usr_city = request.form.get('usrCity')
        usr_state = request.form.get('usrState')
        usr_zip = request.form.get('usrZip')
        if usr_name != "" and usr_email != "" and usr_add1 != "" and usr_add2 != "" or usr_add2 == "" and usr_city != "" and usr_state != "" and usr_zip != "":
            usrInfo = collection.insert_one({"name": usr_name, "email": usr_email, "add1": usr_add1, "add2": usr_add2, "city": usr_city, "state": usr_state, "zip": usr_zip, "items": items})
            return render_template('confirm.html')
        else:
            return("fill the form to process order")

      # print(usr_name, usr_email,usr_add1,usr_add2,usr_city,usr_state,usr_zip)
        #return request.form.get('usrName'),request.form.get('usrEmail'),request.form.get('usrAdd1'),request.form.get('usrAdd2'),request.form.get('usrCity'),request.form.get('usrState'),request.form.get('usrZip')

#Not sure if we should use this seperate GET method or if we should make the ('/confirm') method into our GET.
#Maybe if we do that, we could call it from within the ("/add_user") method on line 42 to run the GET at the same time we render the page?
@app.route('/get_items', methods=["GET"])
def get_items():
    items = collection.find({}, {"items": "Dont know what to put here"})
    return render_template('confirm.html', items = items)
    

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
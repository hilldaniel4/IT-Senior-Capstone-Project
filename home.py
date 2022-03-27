from flask import Flask, render_template, request, flash
app = Flask(__name__)

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
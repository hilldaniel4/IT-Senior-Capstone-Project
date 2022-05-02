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

collection.insert_one({"_id":0, "name":"Shawn"})
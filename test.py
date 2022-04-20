import pymongo
from pymongo import MongoClient
from flask import Flask, render_template, request, flash,redirect, url_for
from flask_pymongo import PyMongo


#Connects python to MongoDB
cluster = MongoClient("mongodb+srv://ShawnTaylor:Seniorcapstone1@seniorcapstone.ksiqj.mongodb.net/GreenGrocery?retryWrites=true&w=majority")
#DB name is GreenGrocery
db = cluster["GreenGrocery"]
#Collections name is test
collection = db["test"]

collection.insert_one({"_id":0, "user_name":"Shawn"})
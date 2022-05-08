# IT-Senior-Capstone-Project
IT Senior Capstone group project using Python + Flask.
Pymongo tools are used to connect the program with a MongoDB cluster which stores and returns data from the app.

The user navigates to the home page and selects items they want to add to their cart. Once they have selected any desired items to add to their cart,
they must fill out the required shipping information in the form below the available products. Once they have finished and press the Confirm Order
button, they are taken to an order confirmation page which has their shipping information and items they selected listed.

To run the app use the following commands:

pip install flask

pip install pymongo

/home/gitpod/.pyenv/versions/3.8.13/bin/python3.8 -m pip install "pymongo[srv]"

export FLASK_ENV=development

FLASK_APP=home.py flask run
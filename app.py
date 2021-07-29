# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]



# -- Routes section --
# INDEX

@app.route('/')
@app.route('/home')

def home():
    return render_template('home.html')


# CONNECT TO DB, ADD DATA

@app.route('/add')
def add():
    # connect to the database
    user = mongo.db.users
    # insert new data
    user.insert({'name' : "Fausto"})
    # return a message to the user
    return "Added User"

@app.route('/events', methods = ["GET", "POST"])
def events():
    if request.method == 'GET':
        return "<h1> Try Again! <h1>"
    else:
        user_name = request.form['first_name']
        user_date = request.form['date']

    
        events.insert({'first_name': user_name, 'date': user_date})
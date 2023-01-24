from petfax import create_app
app = create_app()

""" replaced with code on lines 1-2
# config                    
from flask import Flask
app = Flask(__name__)

# index route
@app.route('/')
def index(): 
    return 'Hello, PetFax!'

# pets index route
@app.route('/pets')
@app.route('/pets/')
def pets(): 
    return 'These are our pets available for adoption!'
"""

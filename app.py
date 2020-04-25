from flask import Flask,render_template
from flask_bootstrap import Booststrap
app = Flask(__name__)
Booststrap(app)
"""
Routes
"""
@app.route('/', methods = ['GET'])
def index():
    return rennder_template('index.html')
if __name__ == '__main__' :
    app.run(debug = True)

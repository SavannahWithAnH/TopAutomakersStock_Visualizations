""" Import Flas directory and test initial set up"""
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
    return 'Hello, world!'

@app.route('/about')
def about():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
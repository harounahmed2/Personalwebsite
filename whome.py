from flask import Flask, render_template, redirect
from datetime import datetime
import os
import sys

app = Flask(__name__)

@app.route('/')
@app.route('/homepage')
def homepage():
    author = "HFiasco"
    name = "Kyle Souders"
    return render_template('homepage.html', author=author, name=name)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

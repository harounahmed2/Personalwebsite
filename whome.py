from flask import Flask, render_template, redirect
from datetime import datetime
import os
import sys

app = Flask(__name__)

@app.route('/')
@app.route('/homepage')
def homepage():
    author = "Haroun Ahmed"
    name = "Kyle Souders"
    return render_template('homepage.html', author=author, name=name)

@app.errorhandler(404)
def page_not_found(e):
    """Custom 404 Page."""
    return render_template('404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    """Custom 500 Page."""
    return render_template('500Error.html'), 500

@app.route('/resume')
def resumemethod():
    return redirect('https://drive.google.com/file/d/11attAO0zFnPnBaDyT1nHgSAUIr7ULuLY/view?usp=sharing', code=302)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

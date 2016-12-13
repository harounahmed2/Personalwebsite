from flask import Flask, render_template
import os
import sys

app = Flask(__name__)

@app.route('/')
def homepage():
    author = "HFiasco"
    name = "Big Nick Magnuson"
    return render_template('index.html', author=author, name=name)



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

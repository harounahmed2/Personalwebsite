from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route('/')
def homepage():
    author = "HFiasco"
    name = "Big Nick Magnuson"
    return render_template('index.html', author=author, name=name)


port = os.getenv('PORT', '5000')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(port))
    app.listen(process.env.PORT || 3000, function())

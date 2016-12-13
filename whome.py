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
    app.run()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "harounpersonalwebsite.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

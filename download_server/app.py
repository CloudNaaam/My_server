from flask import Flask, request, render_template
import os
import html


app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("/hacked.html")

if __name__ == "__main__":
    app.run("0.0.0.0")
from flask import Flask, request, render_template, send_from_directory
import os


app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    return render_template("/hacked.html")

@app.route('/files/<path:filename>')
def download_file(filename):
    # files 디렉터리는 app.py와 같은 위치에 있다고 가정
    return send_from_directory('files', filename)

if __name__ == "__main__":
    app.run("0.0.0.0")
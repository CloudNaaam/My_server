from flask import Flask, request, render_template
import os
import html


app = Flask(__name__, template_folder="templates")
app.secret_key = os.urandom(32)

@app.route("/")
def index():
    data = {
    "method": request.method,
    "url": request.url,
    "client_ip": request.headers.get("X-Forwarded-For") or request.remote_addr,
    "content_type": request.content_type,
    "content_length": request.content_length,
    "headers": dict(request.headers),
    "args": {k: request.args.getlist(k) for k in request.args},
    "form": {k: request.form.getlist(k) for k in request.form},
    "cookies": dict(request.cookies),
    "json_body": request.get_json(silent=True),
}
    raw = request.get_data(cache=False)
    data["raw_preview"] = html.escape(raw[:8192].decode(errors="replace"))
    return render_template("index.html", **data)

if __name__ == "__main__":
    app.run("0.0.0.0")
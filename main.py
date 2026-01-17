import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

REPORT_FOLDER = os.path.join(app.root_path, "static", "files")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/resume")
def resume():
    return render_template("resume.html")

@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(
        REPORT_FOLDER,
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)

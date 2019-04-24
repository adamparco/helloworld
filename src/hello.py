import platform
from flask import Flask, render_template, url_for
app = Flask(__name__)

images = [
    "generic.png",
    "intel.png",
    "arm.jpeg"
]

@app.route("/")
def hello():
    arch = platform.uname()[4]
    image = images[0]
    if "x86" in arch:
        image = images[1]
    elif "arm" in arch:
        image = images[2]

    return render_template('index.html', arch=arch, url=url_for('static', filename= image))

if __name__ == "__main__":
    app.run(host="0.0.0.0")

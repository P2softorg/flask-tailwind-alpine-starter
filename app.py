from flask import Flask
from flask_assets import Bundle, Environment

# Config

app = Flask(__name__)
assets = Environment(app)

# By default, flask looks for files inside the ./static/ folder
# So the path relative to project is "./static/src/main.css"
css = Bundle("src/main.css", output="dist/main.css", filters="postcss")
assets.register("css", css)
css.build()

@app.route("/")
def home():
    return "Hello, Flask!"

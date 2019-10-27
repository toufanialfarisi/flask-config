from flask import Flask
import os

app = Flask(__name__)
app.config.from_object(os.environ["APP_SETTINGS"])
# print("ENVIRONMENT : ", os.environ["APP_SETTINGS"])


@app.route("/")
def index():
    return "<h1>Hallo dunia</h1>"


if __name__ == "__main__":
    app.run()

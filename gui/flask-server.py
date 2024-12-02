# https://www.geeksforgeeks.org/templating-with-jinja2-in-flask/
from flask import Flask, render_template
import json

app = Flask(__name__)


@app.route("/")
def index():
    with open("transcript.json", 'r') as ifile:
        messages = json.load(ifile)
    formatted_messages = [
        f"User {idx % 2 + 1}: {message}" for idx, message in enumerate(messages)]
    return render_template("index.html", messages=formatted_messages)


if __name__ == "__main__":
    app.run()

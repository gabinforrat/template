# https://flask.palletsprojects.com/en/3.0.x/
from flask import Flask, make_response, request, render_template, redirect, Response, abort, url_for

app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return "Hello World"

if __name__ == '__main__':
	app.run(host="0.0.0.0", port="8000", debug=True)

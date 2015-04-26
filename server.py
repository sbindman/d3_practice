from flask import Flask, request, render_template, jsonify, session, flash


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/d3')
def d3():
    return render_template("d3.html")


if __name__ == "__main__":
    app.run( debug=True)
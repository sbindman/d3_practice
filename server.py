from flask import Flask, request, render_template, jsonify, session, flash


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/d3')
def d3():
    return render_template("d3.html")

@app.route('/hex')
def hex():
	return render_template("hex.html")


@app.route('/map')
def map():
	return render_template("map.html")

@app.route('/scooters')
def scooters():
	return render_template("scooters.html")

@app.route('/grid')
def grid():
	return render_template("grid.html")

if __name__ == "__main__":
    app.run( debug=True)
from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    if Dojo.validate(request.form):
        Dojo.save(request.form)
        return redirect("/results")
    else:
        return redirect("/")

@app.route('/results')
def results():
    return render_template("submission.html", results = Dojo.result() )


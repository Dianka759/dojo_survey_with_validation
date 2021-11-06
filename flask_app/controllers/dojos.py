from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    if "user" not in session:
        session["user"] = []
    return render_template("index.html")

@app.route('/submit', methods=["POST"])
def submit():
    if "subscribe" not in request.form:
        temp_user = {
            "name":request.form["name"],
            # "gender":request.form["gender"],
            "location":request.form["location"],
            "favorite_language":request.form["favorite_language"],
            "comment":request.form["comment"],
            "subscribe": "How could you not... :( "
    }
    else :
        temp_user = {
            "name":request.form["name"],
            # "gender":request.form["gender"],
            "location":request.form["location"],
            "favorite_language":request.form["favorite_language"],
            "comment":request.form["comment"],
            "subscribe": "Duh!!! 💙"
    }

    if Dojo.validate(request.form):
        session["user"].append(temp_user)
        session.modified = True
        return redirect("/results")
    else:
        return redirect("/")


@app.route('/results')
def results():
    return render_template("submission.html",user=session["user"])

@app.route("/clear")
def clear():
    session.clear()
    return redirect("/")
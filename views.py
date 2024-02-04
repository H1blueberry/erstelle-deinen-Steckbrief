from flask import Flask, Blueprint, render_template, request, redirect, flash, url_for
from cs50 import SQL
from werkzeug.security import check_password_hash, generate_password_hash
views = Blueprint('views', __name__)

title = ""

info = []

@views.route("/", methods=["GET"])
def x():
    return redirect("home")

@views.route ("/home", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("home.html")
    if request.method == "POST":
        button = request.form.get("add")
        if button != "1":
            print(button)
            global title
            title = request.form.get("title")
            return redirect("steckbrief")
        info.append(request.form.get("info"))
        print(info)
        return render_template("home.html")

@views.route ("/steckbrief", methods=["GET", "POST"])
def steckbrief():
    if request.method == "GET":
        global info
        info2 = info
        return render_template("steckbrief.html", info=info2, title=title)
    if request.method == "POST":
        info = []
        return render_template("home.html")

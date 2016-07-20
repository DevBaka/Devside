# -*- coding: utf-8 -*-
from flask import Flask, url_for, redirect, render_template, request, session, flash, escape
from init import app
from misc.templating import templated

# session['logged_in'] = None

def createNavbar(site):
    foo = {
        "index": ["about me", "kontakt"],
        "about me": ["about me", "kontakt"],
        "kontakt": ["about me", "kontakt"],
        "Programmierung": ["Python", "C#", "C"],
        "Python": ["Python"],
        "kali_linux": ["Installation", "Erste Schritte", "Metasploit", "Port Scan"],
        "login": ["baka"]
    }
    return foo[site]

def username():
    if 'username' in session:
        print "baka " +  escape(session['username'])
    else:
        return "error"


@app.route("/")
@app.route("/Start")
@templated("Start.html")
def index():
    return {"seite": "index", "navbar": createNavbar}

@app.route("/about me")
@templated("about me.html")
def aboutme():
    return {"seite": "about me", "navbar": createNavbar}

@app.route("/kontakt")
@templated("start/kontakt.html")
def kontakt():
    return {"seite": "kontakt", "navbar": createNavbar}

@app.route("/Programmierung")
@templated("dev/Programmierung.html")
def dev():
    return {"seite": "Programmierung", "navbar": createNavbar}

@app.route("/Python")
@templated("dev/python/Python.html")
def Python():
    return {"seite": "Python", "navbar": createNavbar}

@app.route("/kali_linux")
@templated("kali/kali_linux.html")
def kalistart():
    return {"seite": "kali_linux", "navbar": createNavbar}

@app.route("/login", methods=['GET', 'POST'])
@templated("login.html")
def login():
    error = None
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('Python'))
    return render_template('login.html', error=error)

"""
if request.method == "POST":
    username = request.form['username']
    passwd  = request.form['password'] <--- md5, sha2 oder gar was sicheres
    if username in database and passwd == password from username in database:
        session['username'] = 'username'


    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'noob':
            error = "Invalid credentials. Please try again."
        else:
            session['logged_in'] = True
            flash('You wwere just logged in!')
            error = "no error found. Also logged in"
            # return {"seite": "Start", "navbar": createNavbar}
            # return render_template(url_for("Start"))
            return render_template('login.html', error=error)
    return render_template('login.html', error=error) """

@app.route("/logout")
@templated("logout.html")
def logout():
    session.pop('username', None)
    return redirect(url_for("Python"))

@app.route("/dev/py2")
def devpy():
    return render_template("dev/python/py2.html")
@app.route("/todo")
def todo():
    index = """
    <h2> todo </h2>
    <article>
        <p> Die Aside soll wie eine TreeView sein. Alles was zu start gehört soll aufgeklappt werden.
        Was zur Programmierung gehört soll aufgeklappt werden, sobald es angeklickt wird oder man im Header auf Programmierung klickt.
        Darauf sollen Beispielsweise verschiedene Programmiersprachen aufgelistet werden.
        Möglichkeiten:
        <p>-menu/menuitems ... only html/css... contra: kann nit jeder Browser

        <p>zweite möglichkeit:
           <p> If clicked on Dev{include asidedev}...
            <p>they have: Start, Elektrotechnik, Programming new since clicked-->Python, C#, C/C++, Lua, Pawn, Javascript, Kein Java usw...

    </article>
    """
    return redirect("todo")



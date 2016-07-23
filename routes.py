# -*- coding: utf-8 -*-
from flask import Flask, url_for, redirect, render_template, request, session, flash, escape
from init import app
from misc.templating import templated
import sql
import uuid
import sqlite3
#import flask_login
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
    if 'sid' in session:
        print "baka " +  escape(session['sid'])
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
    #print "is the user bereits logged in?: " + sql.isUserLoggedIn(session['sid'])
    error = None
    if request.method == 'POST':
        # session['username'] = request.form['username']
        usermail = request.form["usermail"]
        mgr = sql.SQLmgr()
        userpass = request.form["password"]
        print usermail + " \t " + userpass
        sessionid = uuid.uuid4()
        print "the session of sessions: " + str(sessionid)
        # baka = sql.login(usermail, userpass)
        baka = mgr.login(usermail, userpass)
        print baka
        if baka == None:
            print("Login fehlgeschlagen!")
        else:
            session['sid'] = sessionid
            lolz = escape(session['sid'])
            mgr.set_session( lolz, usermail, userpass)

            print("eingeloggt!")
        return redirect(url_for('Python'))
    return render_template('login.html', error=error)

@app.route("/register", methods=['GET','POST'])
@templated("register.html")
def register():
    if request.method == "POST":
        print "trololololol1: " + sql.usernameInDB
        print "trololololol2: " + sql.usermailInDB
    return ""


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
    baka = escape(session['sid'])
    mgr = sql.SQLmgr()
    print "bakabitch: " + baka
    mgr.logout(str(baka))
    session.pop('sid', None)
    return redirect(url_for("Python"))


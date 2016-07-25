# -*- coding: utf-8 -*-
from flask import Flask, url_for, redirect, render_template, request, session, flash, escape
from init import app
from misc.templating import templated
import sql
import uuid
import passlib
import sqlite3
import bcrypt
from passlib.hash import pbkdf2_sha256
#import flask_login
# session['logged_in'] = None
def createNavbar(site):
    foo = {
        "index": ["about me", "kontakt", "profile"],
        "about me": ["about me", "kontakt"],
        "kontakt": ["about me", "kontakt"],
        "Programmierung": ["Python", "C#", "C"],
        "Python": ["Python"],
        "kali_linux": ["Installation", "Erste Schritte", "Metasploit", "Port Scan"],
        "login": ["baka"],
        "profile": ["about me", "kontakt", "profile", "news"],
        "news": ["about me", "kontakt", "profile", "news"]
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
        usermail = str(request.form["usermail"])
        mgr = sql
        userpass = request.form["password"]
        try:
            etpwd = sql.userpwd(usermail)
            epwd = etpwd[0]
           #userpass = pbkdf2_sha256.encrypt(request.form["password"], rounds=200000, salt_size=16)
            login_mail = str(sql.usermailInDB(usermail))
            print epwd
            upwd = bcrypt.hashpw(userpass.encode('utf-8'), epwd.encode('utf-8'))
            print upwd
            print userpass
            if str(epwd) == str(upwd):
                try:
                    baka = mgr.login(usermail, str(upwd))
                    istrue = baka[0]
                    print istrue
                    if istrue != 1:
                        #if bcrypt.hashpw(userpass.encode('utf-8'), log
                        print("Login fehlgeschlagen!")
                    else:
                        #session['sid'] = sessionid
                        #lolz = escape(session['sid'])
                        #mgr.set_session( lolz, usermail, userpass)
                        username = sql.grepUsernameByMail(usermail)
                        session['username'] = username[0]
                        print("eingeloggt!")
                        return redirect(url_for('profile'))
                except:
                    error="datenbank error"
            else:
                error = "Password Falsch"
        except:
            error = "Email existiert nicht. "
            
            
        return render_template('login.html', error=error)

@app.route("/register", methods=['GET','POST'])
@templated("register.html")
def register():
    error = None
    if request.method == 'POST':
        # session['username'] = request.form['username']
        usermail = request.form["usermail"]
        mgr = sql
        #userpass = pbkdf2_sha256.encrypt(request.form["password"], rounds=200000, salt_size=16)
        userpass = bcrypt.hashpw(request.form["password"], bcrypt.gensalt())
        #userpass = request.form["password"]
        print usermail + " \t " + userpass
        username = request.form["username"]
        # baka = sql.login(usermail, userpass)
        baka = mgr.login(usermail, userpass)
        baka1 = sql.usernameInDB(username)
        baka2 = sql.usermailInDB(usermail)
        print "the bakas!" + baka1 + baka2
        print baka
        if baka1 != "None":
            print("Login fehlgeschlagen!")
        if baka2 != "None":
            print("usermail bereits in datalist")
        else:
            baka4 = sql.register(username, usermail, userpass)
            session['username'] = username
            #session['sid'] = sessionid
            #lolz = escape(session['sid'])
            #mgr.set_session( lolz, usermail, userpass)
            print "baka4: " + baka4
            print("registriert!!")
        return redirect(url_for('profile'))
    return render_template('register.html', error=error)

@app.route("/profile")
@templated("profile.html")
def profile():
    baka = escape(session['username'])
    print("trol jf USERNAME:    !!!! ::::: " + baka )
    return {"seite": "profile", "navbar": createNavbar}

@app.route("/news", methods=['GET','POST'])
@templated("news.html")
def write_news():
    error = None
    if request.method == 'POST':
        autor = session['username']
        titel = request.form['titel']
        datum = request.form['datum']
        entrie = request.form['news']
        sql.write_globalNews(autor, datum, titel, entrie)

            
    return {"seite": "news", "navbar": createNavbar, "error":error}

"""
    error = None
    if request.method == 'POST':
        username = request.form['username']
        usermail = request.form['usermail']
        userpass = request.form['userpass']
        userindb = str(sql.usernameInDB(username))
        print "trololololol1: " + baka
        
        mailindb = str(sql.usermailInDB(usermail))
        print "trololololol2: " + baka2
        
        if userindb and mailindb == None:
            sql.register(username, usermail, userpass)
        else:
            if userindb != None:
                error = "Mail wird bereits benutzt"
            if mailindb != None:
                error = "Username existiert bereits!"
            else:
                error = "Irgendeine ganz andere scheiße im register"
        
        #username = request.form["username"]
      # usermail = request.form["usermail"]
      #  userpass = request.form["userpass"]
        #print "trololololol1: " + sql.usernameInDB(username)
        #print "trololololol2: " + sql.usermailInDB(usermail)
        
    return render_template("register.html", error=error)
"""

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
    #baka = escape(session['username'])
    #mgr = sql.SQLmgr()
    #print "bakabitch: " + baka
    #mgr.logout(str(baka))
    session.pop('username', None)
    return redirect(url_for("Python"))


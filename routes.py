# -*- coding: utf-8 -*-
from flask import Flask, url_for, redirect, render_template, request, session, flash, escape
from init import app
from misc.templating import templated
import sql
import uuid
import passlib
import sqlite3
import bcrypt
import os
from passlib.hash import pbkdf2_sha256
from werkzeug.utils import secure_filename
from flask import send_from_directory
from werkzeug import SharedDataMiddleware
#import flask_login
# session['logged_in'] = None


UPLOAD_FOLDER = 'C:\Users\DevBaka\Source\Repos\Devside\Uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

def createAdminNavbar(site):    
    foo = {}
    return foo[site]

def createNavbar(site):
    dfdfdf = session.get('username')
    if dfdfdf == "baka":
        admintools = ["news writer", "projekt uploader"]
    else:
        admintools = ["", ""]
    foo = {
        "index": ["about me", "kontakt", "news"],
        "about me": ["about me", "kontakt", "news"],
        "kontakt": ["about me", "kontakt", "news"],
        "Programmierung": ["Python", "C#", "C"],
        "Python": ["Python"],
        "kali_linux": ["Installation", "Erste Schritte", "Metasploit", "Port Scan"],
        "login": ["baka"],
        "profile": ["about me", "kontakt", "profile", admintools ],
        "newswriter": ["news","about me", "kontakt", "profile", admintools ],
        "news": ["about me", "kontakt", "news"],
        "Datenbanken": ["SQL Befehle"],
        "SQL Befehle": ["SQL Befehle"],
        "Linux": ["Install Arch Linux"],
        "Projekte": ["Devside", "WeAreOne","Raspi Log Monitoring"],
        "Install Arch Linux": ["Install Arch Linux"]
    }
    return foo[site]

def startside():
    return render_template('asides/startside.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

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

@app.route("/Datenbanken")
@templated("datenbanken/Datenbanken.html")
def Datenbanken():
    return {"seite": "Datenbanken", "navbar": createNavbar}

@app.route("/SQL Befehle")
@templated("datenbanken/sql_commands.html")
def sql_commands():
    return {"seite": "SQL Befehle", "navbar": createNavbar}

@app.route("/Linux")
@templated("Linux/Linux.html")
def Linux():
    return {"seite": "Linux", "navbar": createNavbar}

@app.route("/Install Arch Linux")
@templated("Linux/archinstall.html")
def Archinstall():
    return {"seite": "Install Arch Linux", "navbar": createNavbar}


@app.route("/Projekte")
@templated("Projekte/Projekte.html")
def Projekte():
    return {"seite": "Projekte", "navbar": createNavbar}

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

@app.route("/profile", methods=['GET','POST'])
@templated("profile.html")
def profile():
    fileurl = "none"
    filename = "none"
    try: 
        baka = session['username']
    except:
        baka = "Nicht eingeloggt"
    print baka
    print("trol jf USERNAME:    !!!! ::::: " + baka )
    if baka == 'baka':
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                baka = "No selected file"
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                fileurl = url_for('uploaded_file', filename=filename)
        #return {"seite": "upload", "navbar": createNavbar, "baka":baka, "fileurl":fileurl}
        return {"seite": "profile", "navbar": createNavbar, "baka": baka, "fileurl": fileurl, "filename": filename}
    else:
        return {"seite": "profile", "navbar": createNavbar, "baka": baka}

@app.route("/newswriter", methods=['GET','POST'])
@templated("newswriter.html")
def write_news():
    error = None
    if request.method == 'POST':
        autor = session['username']
        titel = request.form['titel']
        datum = request.form['datum']
        entrie = request.form['news']
        sql.write_globalNews(autor, datum, titel, entrie)

            
    return {"seite": "newswriter", "navbar": createNavbar, "error":error}
@app.route("/news")
@templated("news.html")
def news():
    print("hello world")
    error = None
    i = 0
    baka = {}
    istrue = ""
    autor = ""
    titel = ""
    
    while istrue != None:
        i = i + 1
        #print baka
        istrue = sql.red_news(i)
        tulp = sql.red_news(i)
        print "THE UTLLD D TULPPPEEEEEE!!!: " + str(tulp)
        if tulp != None:
            akdir = {i: [ tulp[1], tulp[2], tulp[3], tulp[4]]}
            baka.update(akdir)

        # lolz = lolz  + str(baka) + "\t\t\t\t\t\t\t"
    return {"seite": "news", "navbar": createNavbar, "baka":baka}

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



@app.route("/upload", methods=['GET','POST'])
@templated("upload.html")
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            baka = "No selected file"
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            fileurl = url_for('uploaded_file', filename=filename)
    return {"seite": "upload", "navbar": createNavbar, "baka":baka, "fileurl":fileurl}

@app.route("/logout")
@templated("logout.html")
def logout():
    #baka = escape(session['username'])
    #mgr = sql.SQLmgr()
    #print "bakabitch: " + baka
    #mgr.logout(str(baka))
    session.pop('username', None)
    return redirect(url_for("Python"))


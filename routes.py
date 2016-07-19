# -*- coding: utf-8 -*-
from flask import Flask
from flask import url_for, redirect, render_template
from init import app
from misc.templating import templated

def createNavbar(site):
    foo = {
        "index": ["about me", "kontakt"],
        "about me": ["about me", "kontakt"],
        "kontakt": ["about me", "kontakt"],
        "Programmierung": ["Python", "C#", "C"],
        "Python": ["Python"]
    }
    return foo[site]


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

@app.route("/Kali Linux")
@templated("kali/Kali Linux.html")
def kalistart():
    return {"seite": "Kali Linux", "navbar": createNavbar}

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


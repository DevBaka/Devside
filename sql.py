import MySQLdb
from constr import Constring as con

baka = con()
z = 0
host = ""
user = ""
pwd = ""
database = ""
for i in baka:
    z = z + 1
    if z == 1:
        host = i
    if z == 2:
        user = i
    if z == 3:
        pwd = i
    if z == 4:
        database = i
def connection():
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print "database version: %s" % data
    db.close()

def isUserLoggedIn(session):
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    cursor.execute("SELECT User_ID FROM users WHERE Session='" + session + "'")
    print cursor.fetchone()
    db.close()
def login(usermail, password):
    connection()
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    try:
        cursor.execute("SELECT User_ID FROM users WHERE usermail='"+ usermail + "'AND userpass='" + password + "'")
        baka = cursor.fetchone()
    except:
        baka = "Login Error"
    db.close()
    return baka

def set_session(session, usermail, userpass):
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    cursor.execute("Update users SET Session_ID='" + session + "' WHERE usermail='"+ usermail + "' AND userpass='" + userpass + "'")

    db.close()
def logout(session):
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    cursor.execute("Update users SET Session_ID=' ' WHERE Session_ID='" + session + "'")
    db.close()
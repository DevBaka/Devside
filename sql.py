import MySQLdb
import mysql
from chirp.pyPEG import code

from constr import Constring as con
from flask import session, escape
import _mysql

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

def login(usermail, password):
    SQLmgr.login2(usermail, password)

def set_session(session, usermail, userpass):
    SQLmgr.set_session2(session, usermail, userpass)
"""
def isUserLoggedIn(session):
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    cursor.execute("SELECT username FROM users WHERE Session_ID='" + str(session) + "'")
    print cursor.fetchone()
    db.close()
def login( usermail, password):
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    cursor.execute("SELECT User_ID FROM users WHERE usermail='"+ usermail + "' AND userpass='" + password + "'")
    # cursor.execute("UPDATE users SET Session_ID='" + session + "' WHERE usermail='" + usermail + "' AND userpass='" + userpass + "'")
    baka = cursor.fetchone()
    db.close()
    return baka

def set_session(session, usermail, userpass):
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    print "benis" + session
    #print session + "\t" + usermail + "\t" + userpass
    #lol = escape(session['sid'])
    cursor.execute("UPDATE users SET Session_ID='" + session+ "' WHERE usermail='"+ usermail + "' AND userpass='" + userpass + "'")
    #cursor.execute("SET SQL_SAFE_UPDATES = 0")
    #cursor.execute("UPDATE users SET Session_ID=%s WHERE usermail=%s AND userpass=%s", (session,usermail,userpass))
    db.close()
def logout(session):
    db = MySQLdb.connect(host, user, pwd, database)
    cursor = db.cursor()
    print session
    cursor.execute("UPDATE users SET Session_ID='' WHERE Session_ID='" + session  + "'")
    db.close()

"""

class SQLif(object):
    def __init__(self, host, user, passw, database):
        self.host = host
        self.user = user
        self.pw = passw
        self.db_name = database


    def __enter__(self):
        self.db = MySQLdb.connect(self.host, self.user, self.pw, self.db_name)
        return self.db.cursor()

    def __exit__(self, type, b, traceback):
        self.db.close()

class SQLmgr(object):
    def __init__(self):
        cstring = con()
        host = cstring[0]
        user = cstring[1]
        passwd = cstring[2]
        data = cstring[3]
        self.db = SQLif(host, user, passwd, data)


    def test(self):
        with self.db as c:
            print c.execute("show tables")
            print c.fetchall()

    def login(self, usermail, password):
        with self.db as c:
            c.execute("SELECT User_ID FROM users WHERE usermail='"+ usermail + "' AND userpass='" + password + "'")
            baka = c.fetchall()
        return baka

    def set_session(self, session, usermail, userpass):
        with self.db as c:
            print "benis" + str(session)
            # print session + "\t" + usermail + "\t" + userpass
            # lol = escape(session['sid'])
            #c.execute("UPDATE users SET Session_ID='baka' WHERE User_ID=1")
            c.query("UPDATE users SET Session_ID=%s WHERE usermail=%s AND userpass=%s", (session,usermail,userpass))
            c.fetchall()
            # cursor.execute("SET SQL_SAFE_UPDATES = 0")
            # cursor.execute("UPDATE users SET Session_ID=%s WHERE usermail=%s AND userpass=%s", (session,usermail,userpass))

    def logout(self, session):
        with self.db as c:
            c.execute("UPDATE users SET Session_ID='' WHERE Session_ID='" + session + "'")


if __name__ == "__main__":
    import readline
    import code
    vars = globals().copy()
    vars.update(locals())
    sh = code.InteractiveConsole(vars)
    sh.interact()
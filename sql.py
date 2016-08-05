#import MySQLdb
#import mysql
#from chirp.pyPEG import code

#from constr import Constring as con
from flask import session, escape
import sqlite3
from passlib.hash import pbkdf2_sha256

#baka = con()
"""
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
"""



def userpwd(usermail):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("SELECT userpass From users WHERE usermail='"+usermail+"'")
    string = c.fetchone()
    db.close()
    print("basdaskdlakldka kdlsa kdlsakdla !!!!! -----> " + str(string))
    return string 

def grepUsernameByMail(usermail):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("SELECT username FROM users WHERE usermail='" + usermail + "'")
    username = c.fetchone()
    db.close()
    return username

def login( usermail, password):
    #epwd = userpwd(usermail)
    #ppwd = pbkdf2_sha256.verify(epwd, hash)
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("SELECT User_ID FROM users WHERE usermail='"+ usermail + "' AND userpass='" + password + "'")
    # cursor.execute("UPDATE users SET Session_ID='" + session + "' WHERE usermail='" + usermail + "' AND userpass='" + userpass + "'")
    baka = c.fetchone()
    db.close()
    return baka

def usernameInDB(username):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("SELECT username FROM users WHERE username='" + username + "'")
    baka = c.fetchone()
    db.close()
    return str(baka)

def usermailInDB(usermail):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("SELECT usermail FROM users WHERE usermail='" +  usermail + "'")
    baka = c.fetchone()
    db.close()
    return str(baka)

def register(username, usermail, userpass):
    print "the user register of the user!!!!: " + username + usermail + userpass
    try:
        db = sqlite3.connect("devside.db")
        c = db.cursor()
        #c.execute("INSERT INTO users(usermail, username, userpass) VALUES('" + str(usermail) + "','" + str(username)  + "','" + str(userpass) + "')")
        c.execute("INSERT INTO users(usermail, username, userpass) VALUES('"+usermail+"','"+username + "','"+userpass +"')")
        baka = "register geklappt!"
       # db.commit()
        db.close()
    except:
        baka = "register error"
    return baka


def set_session(session, usermail, userpass):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    print "benis" + session
    #print session + "\t" + usermail + "\t" + userpass
    #lol = escape(session['sid'])
    c.execute("UPDATE users SET Session_ID='" + session+ "' WHERE usermail='"+ usermail + "' AND userpass='" + userpass + "'")
    #cursor.execute("SET SQL_SAFE_UPDATES = 0")
    #cursor.execute("UPDATE users SET Session_ID=%s WHERE usermail=%s AND userpass=%s", (session,usermail,userpass))
    db.close()

def write_globalNews(autor, datum, titel, news):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("INSERT INTO entries(autor, datum, titel, news) VALUES('" + autor + "','" + datum + "','"+titel+"','"+news+"')")
    db.commit()
    db.close()
def delete_news(titel):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("DELETE FROM entries WHERE titel='" + titel + "'")
    db.commit()
    db.close()

def red_news(entrie_ID):
    db = sqlite3.connect("devside.db")
    c = db.cursor()
    c.execute("SELECT * FROM entries WHERE entrie_ID='"+ str(entrie_ID) +"'")
    baka = c.fetchone()
    db.close()
    return baka


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
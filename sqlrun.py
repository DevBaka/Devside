import sqlite3
import bcrypt

eingabe =""
while eingabe != "exit":
    eingabe = raw_input("eingabe: ")
    if eingabe == "4":
        db = sqlite3.connect("devside.db")
        c = db.cursor()
        c.execute("SELECT * FROM users WHERE usermail='baka@devbaka.de'")
        print c.fetchone()
        db.close()

    if eingabe == "1":

        baka1 = "lol"
        baka2 = "blizzard"
        baka3 = "baka"
        userpass = bcrypt.hashpw(baka3, bcrypt.gensalt())
        conn = sqlite3.connect("devside.db")
        c = conn.cursor()
        c.execute("DROP TABLE users")
        c.execute("""
        CREATE TABLE users(
        User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        usermail TEXT,
        username TEXT,
        userpass TEXT);
        """)
        c.execute("INSERT INTO users(usermail, username, userpass) VALUES ('baka@devbaka.de', '"+ "baka" + "', '" + userpass + "')")
        #c.execute("INSERT INTO users(usermail, username, userpass) VALUES ('"+baka1 + "', '" + baka2 + "', '"+baka3+"')")

        c.execute("SELECT * FROM users ")
        print c.fetchone()
        conn.commit()
        conn.close()
    if eingabe == "2":
        db = sqlite3.connect("devside.db")
        c = db.cursor()
        c.execute("""
        CREATE TABLE entries(
        entrie_ID INTEGER PRIMARY KEY AUTOINCREMENT,
        autor TEXT,
        datum VARCHAR(10),
        titel TEXT,
        news TEXT);""")
        db.commit()
        db.close()
    if eingabe == "3":
        db = sqlite3.connect("devside.db")
        c = db.cursor()
        print c.execute("SELECT * FROM entries")
        c.execute("SELECT * FROM entries WHERE entrie_ID=0")
        baka= c.fetchall
        db.commit()
        print baka
        db.close()
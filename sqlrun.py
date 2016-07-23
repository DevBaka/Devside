import sqlite3

conn = sqlite3.connect("devside.db")
c = conn.cursor()
#c.execute("""
#CREATE TABLE users(
#User_ID INTEGER PRIMARY KEY AUTOINCREMENT,
#usermail CHAR(100) NOT NULL,
#username CHAR(100) NOT NULL,
#userpass CHAR(100) NOT NULL);
#""")
#c.execute("INSERT INTO users(usermail, username, userpass) VALUES ('baka@devbaka.de', 'devbaka', 'baka')")
c.execute("SELECT * FROM users")
print c.fetchone()
conn.commit()
conn.close()
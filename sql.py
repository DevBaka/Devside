import sqlite3

with sqlite3.connect("devbaka.db") as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE users(

    """
"""
users:
    User_ID primary key, int, not null 
    Session int
    usermail text
    passwprt text/pw/encrypted

einträge:
    autor
    titel
    datum  
    text/eintrag

MySql or sqlite3
"""

  #  c.execute("""CREATE TABLE posts(title TEXT, description, TEXT)""")
   # c.execute('INSERT INTO posts VALUES("Good", "I\'m good")')
    #c.execute('INSERT INTO posts VALUES("Well", "I\'m well")')
# https://flask-login.readthedocs.io/en/latest/
#http://www.python-kurs.eu/sql_python.php
#https://docs.python.org/2/library/sqlite3.html
import MySQLdb
from mysqlcon import Constring as con
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
db = MySQLdb.connect(host, user, pwd, database)
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print "database version: %s" % data
db.close()
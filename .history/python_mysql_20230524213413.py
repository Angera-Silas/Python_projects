import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
)
mycursor =mydb.cusor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print
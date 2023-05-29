import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor =mydb.cursor()
mycursor.execute("")
for i in mycursor:
    print(i)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = 
)
mycursor =mydb.cursor()
mycursor.execute("SHOW DATABASES")
for i in mycursor:
    print(i)
import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor =mydb.cursor()
sql = "SELECT * FROM registration"
mycursor.execute(sql)
results = my
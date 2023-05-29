import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM registration where"
mycursor.execute(sql)
results = mycursor.fetchall()
for i in results:
    print(i)
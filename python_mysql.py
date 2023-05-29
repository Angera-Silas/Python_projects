import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "",
    database = "web"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM registration"
mycursor.execute(sql)
results = mycursor.fetchall()
for i in results:
    print(i)
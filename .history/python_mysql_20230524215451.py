import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor = mydb.cursor()
sql = "INSERT INTO regis"
sql = "SELECT * FROM registration WHERE County_Of_residence ='Kakamega'"
mycursor.execute(sql)
results = mycursor.fetchall()
for i in results:
    print(i)
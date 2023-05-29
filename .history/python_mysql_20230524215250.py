import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor = mydb.cursor()
sql = "SELECT * FROM registration WHERE County_Of_residence =%f "
county = ("kakamega,")
mycursor.execute(sql,county)
results = mycursor.fetchall()
for i in results:
    print(i)
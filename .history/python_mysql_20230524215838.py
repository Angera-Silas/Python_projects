import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor = mydb.cursor()
sql = "INSERT INTO registration VALUES(%S,%S)"
val =
sql = "SELECT * FROM registration WHERE County_Of_residence ='Nairobi'"
mycursor.execute(sql)
results = mycursor.fetchall()
for i in results:
    print(i)
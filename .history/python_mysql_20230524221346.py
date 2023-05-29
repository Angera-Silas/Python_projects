import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor = mydb.cursor()
sql = "INSERT INTO registration VALUES(('ovita001','Brian','Ovita','briannathan@gmail.com','2023.04.24','1998.06.28','Kenyan''Vihiga'))"
mycursor.execute(sql)
mydb.commit()
sql = "SELECT * FROM registration"
mycursor.execute(sql)
results = mycursor.fetchall()
for i in results:
    print(i)
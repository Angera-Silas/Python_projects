import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password = "@Dj Bozz 254",
    database = "web"
)
mycursor = mydb.cursor()
sql = "INSERT INTO registration(Username,) VALUES(%S,%S)"
val = [('ovita001','Brian','Ovita','briannathan@gmail.com','','1998.06.28','','Vihiga',''),
       ('kabaji012','Victor','Kabaji','vickabaji@gmail.com','','1993.08.25','','Vihiga','')
       ]
mycursor.executemany(sql,val)
sql = "SELECT * FROM registration"
mycursor.execute(sql)
results = mycursor.fetchall()
for i in results:
    print(i)
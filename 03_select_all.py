import mysql.connector

conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               passwd = "",
                               database = "titanic"
                               )

my_cursor = conn.cursor()
my_cursor.execute("select * from pasajeros")
for bd in my_cursor:
    print(bd)

conn.close()
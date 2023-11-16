import mysql.connector

conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               passwd = ""
                               )

my_cursor = conn.cursor()
my_cursor.execute("show databases")
for bd in my_cursor:
    print(bd[0])

conn.close()
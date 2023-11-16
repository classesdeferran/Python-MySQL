import mysql.connector

conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               passwd = "",
                            #    database = "information_schema"
                               )

my_cursor = conn.cursor()
# my_cursor.execute("use information_schema")
my_cursor.execute("show tables")
for bd in my_cursor:
    print(bd[0])

conn.close()
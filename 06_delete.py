import mysql.connector

conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               passwd = "",
                               database = "titanic"
                               )

my_cursor = conn.cursor()
my_cursor.execute("DELETE FROM pasajeros WHERE name LIKE '%Lois Lane%'")
conn.commit()
conn.close()
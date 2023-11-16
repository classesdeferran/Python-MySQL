import mysql.connector

conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               passwd = "",
                               database = "titanic"
                               )

my_cursor = conn.cursor()
my_cursor.execute("UPDATE pasajeros SET home_dest = 'Mataró' WHERE pclass = 4")
conn.commit()
conn.close()
import mysql.connector

conn = mysql.connector.connect(host = "localhost",
                               user = "root",
                               passwd = "",
                               database = "titanic"
                               )

my_cursor = conn.cursor()
datos = ( 4, 1, 'Peter Parker', 'araña', 25,0,0,'00001', '0', '0','M', '','','' )
query = ('''INSERT INTO pasajeros 
                  VALUES ( %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s,%s )''' )
my_cursor.execute(query, datos)
conn.commit()
conn.close()
import mysql.connector
import mysql.connector
from mysql.connector import pooling

# global variables
user_type = None
screen_number = None
logged_user = None
if __name__ == "__main__":
    connection_pool = pooling.MySQLConnectionPool( pool_name = "beltline_pool",
                                                                   pool_size = 5,
                                                                   pool_reset_session = True,
                                                                   host = 'localhost',
                                                                   database = 'Beltline',
                                                                   user = 'root',
                                                                   password = '',
                                                                   use_pure = True)
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        info = connection_object.get_server_info()
        print("Connected to MySQL server: ",info)
    else:
        print("Database not connected")
user_name = 'clu319'
pwd = '12345678'
lname = 'lu'
fname = 'cb'
cursor = connection_object.cursor()
#query3 = "insert into user values (\'"+ user_name + "\',\'" + pwd + "\'," + "\'Pending\'" + ",\'" + fname + "\',\'" + lname + "\',\'User\');"
sql = "select * from user;"
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    print(row)


if(connection_object.is_connected()):
    cursor.close()
    connection_object.close()
    print("MySQL connection is closed")

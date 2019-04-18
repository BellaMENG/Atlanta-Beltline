import mysql.connector
import mysql.connector
from mysql.connector import pooling
from helper import hash_password

if __name__ == "__main__":
    connection_pool = pooling.MySQLConnectionPool( pool_name = "beltline_pool",
                                                                   pool_size = 5,
                                                                   pool_reset_session = True,
                                                                   host = 'localhost',
                                                                   database = 'beltline_version2',
                                                                   user = 'root',
                                                                   password = '',
                                                                   use_pure = True)
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        info = connection_object.get_server_info()
        print("Connected to MySQL server: ",info)
    else:
        print("Database not connected")


sql = "select Username,Password from user;"

connection_object = connection_pool.get_connection()
if connection_object.is_connected():
    db_Info = connection_object.get_server_info()
    print("user_login.py login() Connected to MySQL server: ",db_Info)
else:
    print("user_login.py login() Not Connected ")
cursor = connection_object.cursor()
cursor.execute(sql)
result = cursor.fetchall()
for row in result:
    user_name,pwd = row
    pwd = hash_password(pwd)
    sql = "update user set Password = pwd where Username = user_name;"
    cursor.execute(sql)
connection_object.commit()
if(connection_object.is_connected()):
    cursor.close()
    connection_object.close()
    print("MySQL connection is closed")

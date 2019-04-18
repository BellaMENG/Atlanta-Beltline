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
user_name = 'sunxiaochuan'
pwd = '12345678'
lname = 'lu'
fname = 'cb'
first_name = 'haha'
last_name = 'xixi'
phone = '123-456-7890'

def isManager(suser_name):
    query1 = "SELECT count(*) FROM manager WHERE Username = \'" + user_name + "\';"
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        db_Info = connection_object.get_server_info()
        print("user_login.py login() Connected to MySQL server: ",db_Info)
    else:
        print("user_login.py login() Not Connected ")
    cursor = connection_object.cursor()
    cursor.execute(query1)
    result = cursor.fetchall()
    if(connection_object.is_connected()):
        cursor.close()
        connection_object.close()
        print("MySQL connection is closed")
    if result[0][0] == 0:
        return False
    else:
        return True

# query1 = "SELECT count(*) FROM visitor WHERE Username = \'" + user_name + "\';"
# connection_object = connection_pool.get_connection()
# if connection_object.is_connected():
#     db_Info = connection_object.get_server_info()
#     print("user_login.py login() Connected to MySQL server: ",db_Info)
# else:
#     print("user_login.py login() Not Connected ")
# cursor = connection_object.cursor()
# cursor.execute(query1)
# result = cursor.fetchall()
# if(connection_object.is_connected()):
#     cursor.close()
#     connection_object.close()
#     print("MySQL connection is closed")
# print(type(result[0][0]))
# print(result[0][0])

print(isManager(user_name))

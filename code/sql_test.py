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
user_name = 'manager2'
pwd = '12345678'
lname = 'lu'
fname = 'cb'
first_name = 'haha'
last_name = 'xixi'
phone = '123-456-7890'

# mydb = mysql.connector.connect(
#   host="localhost",       # 数据库主机地址
#   user="root",    # 数据库用户名
#   passwd='',
#   database = 'Beltline'
# )
cursor = connection_object.cursor()
sql = "Update user set Lastname= \'" + last_name + "\', Firstname= \'" + first_name + "\' where Username= \'" + user_name + "';"
sql2 = "Update employee set Phone= \'" + phone +  "\' where Username= \'" + user_name + "\';"
print(sql)
cursor.execute(sql)
connection_object.commit()
cursor.execute(sql2)
connection_object.commit()

if(connection_object.is_connected()):
    cursor.close()
    connection_object.close()
    print("MySQL connection is closed")


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

mydb = mysql.connector.connect(
  host="localhost",       # 数据库主机地址
  user="root",    # 数据库用户名
  passwd='',
  database = 'Beltline'
)
cursor = mydb.cursor()
sql = "call get_transit_options(\'\',\'\',0,100);"
print(sql)
cursor.execute(sql,multi=True)
result = cursor.fetchall()
for row in result:
    print(row)
# for result in cursor.stored_results():
#     print(result.fetchall())

if(connection_object.is_connected()):
    cursor.close()
    connection_object.close()
    print("MySQL connection is closed")


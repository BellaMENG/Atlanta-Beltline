import mysql.connector

# global variables
user_type = None
screen_number = None
logged_user = None
if __name__ == "__main__":
    connection_pool = mysql.connector.pooling.MySQLConnectionPool( pool_name = ,
                                                                   pool_size = ,
                                                                   pool_reset_session = True,
                                                                   host = ,
                                                                   database = ,
                                                                   user = ,
                                                                   password = ,
                                                                   use_pure = True)
    connection_object = connection_pool.get_connection()
    if connection_object.is_connected():
        info = connection_object.get_server_info()
        print("Connected to MySQL server: ",info)
    else:
        print("Database not connected")
    

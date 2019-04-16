import mysql.connector
import mysql.connector
from mysql.connector import pooling

# global variables
user_type = None
screen_number = None
logged_user = None

import user_login,register_navigation,register_user,register_visitor,register_employee,register_employee_v
import user_functionality,admin_functionality,admin_functionality_v,manager_functionality,manager_functionality_v,staff_functionality,staff_functionality_v,visitor_functionality
import user_take_transit,user_transit_history
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

    #user_login.render()
    logged_user = 'cluah'
    user_transit_history.render()

    while True:
        if screen_number == 1:
            user_login.render()
        elif screen_number == 2:
            register_navigation.render()
            print("screen number after register_navigation:",screen_number)
        elif screen_number == 3:
            register_user.render()
        elif screen_number == 4:
            register_visitor.render()
        elif screen_number == 5:
            register_employee.render()
        elif screen_number == 6:
            register_employee_v.render()
        elif screen_number == 7:
            user_functionality.render()
            print("screen number after user_functionality:",screen_number)

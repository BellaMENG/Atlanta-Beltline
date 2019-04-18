import mysql.connector
import mysql.connector
from mysql.connector import pooling

# global variables
user_type = None
screen_number = None
logged_user = None

import user_login,register_navigation,register_user,register_visitor,register_employee,register_employee_v
import user_functionality,admin_functionality,admin_functionality_v,manager_functionality,manager_functionality_v,staff_functionality,staff_functionality_v,visitor_functionality
import user_take_transit,user_transit_history,employee_manage_profile
import administrator_manage_user,administrator_manage_site,administrator_edit_site,administrator_create_site, administrator_manage_transit
import administrator_edit_transit,administrator_create_transit
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

    #user_login.render()
    # logged_user = 'manager2'
    # administrator_create_transit.render()
    # print("screen number after test page:",screen_number)

    # user_login.render()
    # print("screen number after user_login:",screen_number)
    # print("user type after user_login:",user_type)
    # print("user name after user_login",logged_user)

    user_type = "Administrator"
    logged_user = 'james.smith'
    screen_number = 8

    while True:
        print("loop running ",screen_number)
        if screen_number == 1:
            user_login.render()
            print("screen number after user_login:",screen_number)
            print("user type after user_login:",user_type)
            print("user name after user_login",logged_user)

        elif screen_number == 2:
            register_navigation.render()
            print("screen number after register_navigation:",screen_number)

        elif screen_number == 3:
            register_user.render()
            print("screen number after register_user:",screen_number)

        elif screen_number == 4:
            register_visitor.render()
            print("screen number after register_visitor:",screen_number)

        elif screen_number == 5:
            register_employee.render()
            print("screen number after register_employee:",screen_number)

        elif screen_number == 6:
            register_employee_v.render()
            print("screen number after register_employee_v:",screen_number)

        elif screen_number == 7:
            user_functionality.render()
            print("screen number after user_functionality:",screen_number)

        elif screen_number == 8:
            admin_functionality.render()
            print("screen number after admin_functionality:",screen_number)

        elif screen_number == 9:
            admin_functionality_v.render()
            print("screen number after admin_functionality_v:",screen_number)

        elif screen_number == 10:
            manager_functionality.render()
            print("screen number after manager_functionality:",screen_number)

        elif screen_number == 11:
            manager_functionality_v.render()
            print("screen number after manager_functionality_v:",screen_number)

        elif screen_number == 12:
            staff_functionality.render()
            print("screen number after staff_functionality:",screen_number)

        elif screen_number == 13:
            staff_functionality_v.render()
            print("screen number after staff_functionality_v:",screen_number)

        elif screen_number == 14:
            visitor_functionality.render()
            print("screen number after visitor_functionality:",screen_number)

        elif screen_number == 15:
            user_take_transit.render()
            print("screen number after user_take_transit:",screen_number)

        elif screen_number == 16:
            user_transit_history.render()
            print("screen number after user_transit_history:",screen_number)

        elif screen_number == 17:
            employee_manage_profile.render()
            print("screen number after employee_manage_profile:",screen_number)

        elif screen_number == 18:
            administrator_manage_user.render()
            print("screen number after administrator_manage_user:",screen_number)

        elif screen_number == 19:
            administrator_manage_site.render()
            print("screen number after administrator_manage_site:",screen_number)

        elif screen_number == 20:
            administrator_edit_site.render(argv1,argv2)
            print("screen number after administrator_edit_site:",screen_number)

        elif screen_number == 21:
            administrator_create_site.render()
            print("screen number after administrator_create_site:",screen_number)

        elif screen_number == 22:
            administrator_manage_transit.render()
            print("screen number after administrator_manage_transit:",screen_number)

        elif screen_number == 23:
            administrator_edit_transit.render(argv1,argv2,argv3)
            print("screen number after administrator_edit_transit:",screen_number)

        elif screen_number == 24:
            administrator_create_transit.render()
            print("screen number after screen_number:",screen_number)
        



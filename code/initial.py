import mysql.connector
import mysql.connector
from mysql.connector import pooling

# global variables
user_type = None
screen_number = None
logged_user = None
selected_event25 = None
selected_date29 = None
site_name29 = None
selected_event31 = None
selected_event33 = None
selected_site35 = None
Quit = False
argv1 = None
argv2 = None
argv3 = None

# event: event.Name, event.StartDate, event.SiteName

import user_login,register_navigation,register_user,register_visitor,register_employee,register_employee_v
import user_functionality,admin_functionality,admin_functionality_v,manager_functionality,manager_functionality_v,staff_functionality,staff_functionality_v,visitor_functionality
import user_take_transit,user_transit_history, employee_manage_profile
import manager_manage_event, manager_view_or_edit_event, manager_create_event, manager_manage_staff
import manager_site_report, manager_daily_detail, staff_view_schedule, staff_event_detail
import visitor_explore_event, visitor_event_detail, visitor_explore_site
import visitor_transit_detail, visitor_site_detail, visitor_visit_history, administrator_manage_user
import administrator_manage_site, administrator_edit_site, administrator_create_site, administrator_manage_transit
import administrator_edit_transit, administrator_create_transit
if __name__ == "__main__":
    connection_pool = pooling.MySQLConnectionPool( pool_name = "beltline_pool",
                                                                   pool_size = 5,
                                                                   pool_reset_session = True,
                                                                   host = 'localhost',
                                                                   database = 'beltline_version2',
                                                                   user = 'bella',
                                                                   password = '',
                                                                   use_pure = True)
    # connection_object = connection_pool.get_connection()
    # if connection_object.is_connected():
    #     info = connection_object.get_server_info()
    #     print("Connected to MySQL server: ",info)
    # else:
    #     print("Database not connected")

    user_login.render()

    while not Quit:
        if screen_number == 1:
            user_login.render()
        elif screen_number == 2:
            register_navigation.render()
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
        elif screen_number == 8:
            admin_functionality.render()
        elif screen_number == 10:
            manager_functionality.render()
        elif screen_number == 11:
            manager_functionality_v.render()
        elif screen_number == 12:
            staff_functionality.render()
        elif screen_number == 13:
            staff_functionality_v.render()
        elif screen_number == 14:
            visitor_functionality.render()
        elif screen_number == 15:
            user_take_transit.render()
        elif screen_number == 16:
            user_transit_history.render()
        elif screen_number == 17:
            employee_manage_profile.render()
        elif screen_number == 18:
            administrator_manage_user.render()
        elif screen_number == 19:
            administrator_manage_site.render()
        elif screen_number == 20:
            administrator_edit_site.render(argv1,argv2)
        elif screen_number == 21:
            administrator_create_site.render()
        elif screen_number == 22:
            administrator_manage_transit.render()
        elif screen_number == 23:
            administrator_edit_transit.render(argv1,argv2,argv3)
        elif screen_number == 24:
            administrator_create_transit.render()
        elif screen_number == 25:
            manager_manage_event.render()
        elif screen_number == 26:
            manager_view_or_edit_event.render()
        elif screen_number == 27:
            manager_create_event.render()
        elif screen_number == 28:
            manager_manage_staff.render()
        elif screen_number == 29:
            manager_site_report.render()
        elif screen_number == 30:
            manager_daily_detail.render()
        elif screen_number == 31:
            staff_view_schedule.render()
        elif screen_number == 32:
            staff_event_detail.render()
        elif screen_number == 33:
            visitor_explore_event.render()
        elif screen_number == 34:
            visitor_event_detail.render()
        elif screen_number == 35:
            visitor_explore_site.render()
        elif screen_number == 36:
            visitor_transit_detail.render()
        elif screen_number == 37:
            visitor_site_detail.render()
        elif screen_number == 38:
            visitor_visit_history.render()

    # if (connection_object.is_connected()):
    #     connection_object.close()
    #     print("MySQL connection is closed")


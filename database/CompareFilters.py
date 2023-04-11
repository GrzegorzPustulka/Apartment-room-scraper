from database.sshConfig import create_ssh_tunnel
import MySQLdb
from dotenv import load_dotenv
import os
# from emailSender.emailSender import email_sender


def compare_filters_new_apartment(city, ad, area, district, olx_rooms, price, indicators):
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB'),
        )
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        for user in users:
            user_id = user[0]
            user_email = user[1]
            cur.execute(f'SELECT * FROM apartment_filters WHERE id_user={user_id}')
            filters = cur.fetchall()

            for filter_ in filters:
                city_filter = filter_[1]
                price_filter = filter_[2]
                area_filter = filter_[3]
                # bedzie trzeba dodac rozdzielenie zeby bylo multi district i room_type
                district_filter = filter_[4]
                room_type_filter = filter_[5]

                if price <= price_filter and area >= area_filter and city == city_filter and \
                        district == district_filter and olx_rooms == room_type_filter:
                    print(ad)
                    # email_sender()

        conn.commit()
        cur.close()
        conn.close()


def compare_filters_new_room(city, ad, district, room_type, price, additional_fees):
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB93+'),
        )
        cur = conn.cursor()
        cur.execute('SELECT * FROM users')
        users = cur.fetchall()
        for user in users:
            user_id = user[0]
            user_email = user[1]
            cur.execute(f'SELECT * FROM apartment_filters WHERE id_user={user_id}')
            filters = cur.fetchall()

            for filter_ in filters:
                price_filter = filter_[2]
                city_filter = filter_[3]
                # bedzie trzeba dodac rozdzielenie zeby bylo multi district i room_type
                district_filter = filter_[4]
                room_type_filter = filter_[5]

                if price + additional_fees <= price_filter and district == district_filter and \
                        room_type == room_type_filter and city_filter == city:
                    print(ad)
                    # email_sender()

        conn.commit()
        cur.close()
        conn.close()
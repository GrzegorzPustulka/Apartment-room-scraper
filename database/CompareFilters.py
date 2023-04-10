from database.sshConfig import create_ssh_tunnel
import MySQLdb
from dotenv import load_dotenv
import os
from emailSender.emailSender import email_sender


def compare_filters_new_apartment():
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

                cur.execute(f'SELECT * FROM new_apartment WHERE city = {city_filter}')
                apartments = cur.fetchall()

                for apartment in apartments:
                    area_apartment = apartment[3]
                    district_apartment = apartment[4]
                    room_type_apartment = apartment[5]
                    total_apartment = apartment[9]

                    if total_apartment <= price_filter and area_apartment >= area_filter and \
                            district_apartment == district_filter and room_type_apartment == room_type_filter:
                        email_sender()

        conn.commit()
        cur.close()
        conn.close()

from database.sshConfig import create_ssh_tunnel
import MySQLdb
from dotenv import load_dotenv
import os


def insert_apartments_db(ads, city):
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB'),
        )
        cur = conn.cursor()
        cur.execute(f'TRUNCATE TABLE apartment_{city};')
        for apartment in ads:
            link = apartment.link
            source = apartment.source
            area = apartment.area
            district = apartment.district
            room_type = apartment.room_type
            price = apartment.price
            rent = apartment.rent
            bills = apartment.bills
            total = apartment.total
            indicators = apartment.indicators
            date = apartment.date
            images = ",".join(apartment.images)

            insert_query = f"INSERT INTO apartment_{city} (link, source, area, district, room_type, price, rent, bills, total, indicators, date, images) VALUES ('{link}','{source}', '{area}', '{district}', '{room_type}', '{price}', '{rent}', '{bills}', '{total}','{indicators}','{date}', '{images}')"
            cur.execute(insert_query)
        conn.commit()
        cur.close()
        conn.close()


def insert_rooms_db(ads, city):
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB'),
        )
        cur = conn.cursor()
        cur.execute(f'TRUNCATE TABLE room_{city};')
        for flat in ads:
            link = flat.link
            source = flat.source
            district = flat.district
            room_type = flat.room_type
            price = flat.price
            bills = flat.bills
            total = flat.total
            date = flat.date
            images = ",".join(flat.images)

            insert_query = f"INSERT INTO room_{city} (link, source, district, room_type, price, bills, total, date, images) VALUES ('{link}','{source}', '{district}', '{room_type}', '{price}', '{bills}', '{total}','{date}', '{images}')"
            cur.execute(insert_query)
        conn.commit()
        cur.close()
        conn.close()


def add_user(email):
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB'),
        )
        cur = conn.cursor()
        insert_query = f"INSERT INTO users (email) VALUES ('{email}')"
        cur.execute(insert_query)
        conn.commit()
        cur.close()


def add_new_apartment(city, link, area, district, room_type, price, rent, bills, total, indicators):
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB'),
        )
        cur = conn.cursor()
        city_value = city
        delete_query = f"DELETE FROM new_apartment WHERE city = '{city_value}'"
        cur.execute(delete_query)
        insert_query = f"INSERT INTO new_apartment(link,city, area, district, room_type, price, rent, bills, total, indicators) VALUES ('{link}','{city}','{area}', '{district}', '{room_type}', '{price}', '{rent}', '{bills}','{total}', '{indicators}')"
        cur.execute(insert_query)
        conn.commit()
        cur.close()

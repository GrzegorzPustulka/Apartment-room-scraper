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
            area = apartment.area
            district = apartment.district
            type_room = apartment.type_room
            price = apartment.price
            rent = apartment.rent
            bills = apartment.bills
            total = apartment.total
            image = ",".join(apartment.image)

            insert_query = f"INSERT INTO apartment_{city} (link, area, district, type_room, price, rent, bills, total, image) VALUES ('{link}', {area}, '{district}', '{type_room}', {price}, {rent}, {bills}, {total}, '{image}')"
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
            district = flat.district
            room = flat.room
            price = flat.price
            bills = flat.bills
            total = flat.total
            image = ",".join(flat.image)

            insert_query = f"INSERT INTO room_{city} (link, district, room, price, bills, total, image) VALUES ('{link}', '{district}', '{room}', {price}, {bills}, {total}, '{image}')"
            cur.execute(insert_query)
        conn.commit()
        cur.close()
        conn.close()

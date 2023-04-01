from database.sshConfig import create_ssh_tunnel
import MySQLdb
from dotenv import load_dotenv
import os


def create_room_table(city: str) -> None:
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB'),
        )
        cur = conn.cursor()
        create_table_query = f"""
        CREATE TABLE room_{city} (
            ID INT NOT NULL AUTO_INCREMENT,
            link VARCHAR(255) NOT NULL,
            district VARCHAR(255) NULL,
            room VARCHAR(255) NULL,
            price FLOAT NOT NULL,
            bills FLOAT NULL,
            total FLOAT NULL,
            image VARCHAR(16384) NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB;
        """
        cur.execute(create_table_query)
        conn.commit()
        cur.close()
        conn.close()


def create_apartment_table(city: str) -> None:
    load_dotenv()
    with create_ssh_tunnel() as tunnel:
        conn = MySQLdb.connect(
            user=os.getenv('USER'),
            passwd=os.getenv('PASSWD'),
            host='127.0.0.1', port=tunnel.local_bind_port,
            db=os.getenv('DB'),
        )
        cur = conn.cursor()
        create_table_query = f"""
        CREATE TABLE apartment_{city} (
            ID INT NOT NULL AUTO_INCREMENT,
            link VARCHAR(255) NOT NULL,
            area FLOAT NULL,
            district VARCHAR(255) NULL,
            type_room VARCHAR(255) NULL,
            price FLOAT NOT NULL,
            rent FLOAT NULL,
            bills FLOAT NULL,
            total FLOAT NULL,
            image VARCHAR(16384) NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB;
        """
        cur.execute(create_table_query)
        conn.commit()
        cur.close()
        conn.close()

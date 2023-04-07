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
            source VARCHAR(30) NOT NULL,
            link VARCHAR(255) NOT NULL,
            district VARCHAR(255) NULL,
            room_type VARCHAR(255) NULL,
            price FLOAT NOT NULL,
            bills FLOAT NULL,
            total FLOAT NULL,
            date VARCHAR(255) NULL,
            images VARCHAR(16384) NULL,
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
            source VARCHAR(30) NOT NULL,
            area FLOAT NULL,
            district VARCHAR(255) NULL,
            room_type VARCHAR(255) NULL,
            price FLOAT NOT NULL,
            rent FLOAT NULL,
            bills FLOAT NULL,
            total FLOAT NULL,
            indicators BOOLEAN DEFAULT FALSE,
            date VARCHAR(255) NULL,
            images VARCHAR(2048) NULL,
            PRIMARY KEY (id)
        ) ENGINE=InnoDB;
        """
        cur.execute(create_table_query)
        conn.commit()
        cur.close()
        conn.close()

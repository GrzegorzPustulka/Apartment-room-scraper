import sshtunnel
from dotenv import load_dotenv
import os


sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0


def create_ssh_tunnel():
    load_dotenv()
    return sshtunnel.SSHTunnelForwarder(
        (os.getenv('SSH')),
        ssh_username=os.getenv('SSH_USERNAME'),
        ssh_password=os.getenv('SSH_PASSWORD'),
        remote_bind_address=(os.getenv('HOST'), int(os.getenv('PORT')))
    )

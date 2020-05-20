from typing import Tuple
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import definitions as defs
import os

CREDENTIALS_PATH = defs.CONF_PATH + "/db.credentials"
DB_IP = "theinventorydb-xajse.mongodb.net"


def get_db_client() -> MongoClient:
    # keep the actual credentials in memory as short as possible

    username, password = get_db_credentials()
    client = MongoClient(
        f"mongodb+srv://{username}:{password}@{DB_IP}" +
        f"/test?retryWrites=true&w=majority")

    return client


def get_db_credentials() -> Tuple[str, str]:


    try:
        with open(CREDENTIALS_PATH) as f:
            username = f.readline().strip()
            password = f.readline().strip()

        return username, password

    except FileNotFoundError as e:

        # Get the credentials from the environment for Travis builds
        username = os.environ.get('mongo-user')
        password = os.environ.get('mongo-pass')

        if username is None or password is None:
            print("Credentials not found in file or environment")
            raise e



def try_db_connection() -> bool:
    db_client = get_db_client()

    # Check if the database connection is actually available. Copied from
    # https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
    try:
        db_client.admin.command('ismaster')
        return True

    except ConnectionFailure:
        return False

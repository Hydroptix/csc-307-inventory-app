from typing import Tuple
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import definitions as defs
import os
from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import random
app = Flask(__name__)
CORS(app)


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

    except FileNotFoundError as e:

        # Get the credentials from the environment for Travis builds
        username = os.environ.get('MongoUser')
        password = os.environ.get('MongoPass')

        if username is None or password is None:
            print("Credentials not found in file or environment")
            raise e

    return username, password


def try_db_connection() -> bool:
    db_client = get_db_client()

    # Check if the database connection is actually available. Copied from
    # https://pymongo.readthedocs.io/en/stable/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient
    try:
        db_client.admin.command('ismaster')
        return True

    except ConnectionFailure:
        return False

users = { 
   'users_list' :
   [
      { 
         'id' : 'xyz789',
         'user' : 'Charlie',
         'artist': 'Frank Ocean',
         'title': 'Nike',
      },
      {
         'id' : 'abc123', 
         'user': 'Mac',
         'artist': 'J Cole',
         'title': 'Brackets',
      },
      {
         'id' : 'ppp222', 
         'user': 'Mac',
         'artist': 'Tidus',
         'title': 'No Limitations',
      }, 
      {
         'id' : 'yat999', 
         'user': 'Dee',
         'artist': 'Adele',
         'title': 'Hello',
      },
      {
         'id' : 'zap555', 
         'user': 'Dennis',
         'artist': 'Kendrick Lamar',
         'title': 'Swimming Pools',
      }
   ]
}

def generate_ID():
    new_ID = ""
    for i in range(6):
        new_ID = new_ID + str(random.randint(0,9))
    return new_ID

@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('user')
      if search_username:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['user'] == search_username:
               subdict['users_list'].append(user)
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      for user in users['users_list']:
          if user['user'] == userToAdd['user']:
              userToAdd['id'] = user['id']
      if 'id' not in userToAdd.keys():
          userToAdd['id'] = generate_ID()
      users['users_list'].append(userToAdd)
      resp = jsonify(userToAdd), 201
      return resp


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      users_id = {'users_list' : [] }
      if id :
         for user in users['users_list']:
           if user['id'] == id:
              users_id['users_list'].append(user)
         return (users_id)
      return users
   elif request.method == 'DELETE':
      if id :
         for i in range(len(users['users_list'])):
           if users['users_list'][i]['id'] == id:
              del users['users_list'][i]
              return users
      return (users)

@app.route('/')
def hello_world():
    return 'Hello, World!'

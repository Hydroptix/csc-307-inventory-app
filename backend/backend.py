from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app)


users = {
   'users_list' :
   [
      {
         'id' : 'xyz789',
         'user' : 'Charlie',

      },
      {
         'id' : 'ppp222',
         'user': 'Mac'
      },
      {
         'id' : 'yat999',
         'user': 'Dee'
      },
      {
         'id' : 'zap555',
         'user': 'Dennis'
      }
   ]
}
songs_list = {
   'songs_list' :
   [
      {
         'song_id': "1",
         'artist': 'Frank Ocean',
         'title': 'Nike',
      },
      {
         'song_id':"2",
         'artist': 'J Cole',
         'title': 'Brackets',
      },
      {
         'song_id':"3",
         'artist': 'Tidus',
         'title': 'No Limitations',
      },
      {
         'song_id':"4",
         'artist': 'Adele',
         'title': 'Hello',
      },
      {
         'song_id':"5",
         'artist': 'Kendrick Lamar',
         'title': 'Swimming Pools',
      }
   ]
}

inventory_list = {
   'inventory_list' :
   [
      {"inventory_id":"1",
      "ownerid":"xyz789"
       }

   ]
}

playlists_list = {
   'playlist_lists' :
   [
      {"playlist_id":"1",
      "name":"bangers",
      "inventory_id":"1"
   }
   ]
}
playlist_songs = {
   'playlist_songs' :
   [
      {"entry_id":"1",
       "song_id":"1",
       "playlist_id":"1"}
   ]
}
inventory_songs = {
   'inventory_songs' :
   [
      {
         "entry_id":"1",
         "inventory_id":"1",
         "song_id":"1"
      },
{
         "entry_id":"2",
         "inventory_id":"1",
         "song_id":"2"
      }
   ]
}


@app.route('/users', methods=['GET', 'POST'])
def get_users():
   if request.method == 'GET':
      search_username = request.args.get('user')
      if search_username:
         subdict = {'users_list' : []}
         for user in users['users_list']:
            if user['user'] == search_username:
               subdict['users_list'].append(user.get('user'))
         return subdict
      return users
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      return resp


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      if id:
         for user in users['users_list']:
           if user['id'] == id:
               for inventory in inventory_list['inventory_list']:
                  if inventory['ownerid'] == id:
                     return jsonify(user,inventory)
         return ({})
      return users
   elif request.method == 'DELETE':
      if id :
         for i in range(len(users['users_list'])):
           if users['users_list'][i]['id'] == id:
              del users['users_list'][i]
              return users
      return ({})


@app.route('/users/<id>/inv', methods=['GET','DELETE'])
def get_inv(id):
   if request.method == 'GET':
      if id:
         invid = []
         final_list = []
         for inventory in inventory_list['inventory_list']:
            if inventory['ownerid'] == id:
               invid.append(inventory['inventory_id'])
         for song in inventory_songs['inventory_songs']:
            if song['inventory_id'] in invid:
               final_list.append(song)
         return jsonify(final_list)
      return ({})


@app.route('/inv',methods = ['GET','DELETE'])
def get_invs():
   if request.method == 'GET':
      search_inv = request.args.get('inv')
      if search_inv:
         subdict = {'inventory_list' : [], "songs_list": []}
         invids = []
         songids = []
         for inventory in inventory_list['inventory_list']:
            if inventory['ownerid'] == search_inv:
               subdict['inventory_list'].append(inventory)
               invids.append(inventory.get('inventory_id'))
         for song in inventory_songs['inventory_songs']:
            if song['inventory_id'] in invids:
               songids.append(song['song_id'])
         for song in songs_list['songs_list']:
            if song['song_id'] in songids:
               subdict["songs_list"].append(song)
         return subdict
      return jsonify(inventory_list,songs_list)
   elif request.method == 'POST':
      userToAdd = request.get_json()
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      return resp


@app.route('/')
def hello_world():
    return 'Hello world'


from flask import Flask
from flask import request
from flask import jsonify
app = Flask(__name__)


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
      users['users_list'].append(userToAdd)
      resp = jsonify(success=True)
      return resp


@app.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
   if request.method == 'GET':
      if id :
         for user in users['users_list']:
           if user['id'] == id:
              return user
         return ({})
      return users
   elif request.method == 'DELETE':
      if id :
         for i in range(len(users['users_list'])):
           if users['users_list'][i]['id'] == id:
              del users['users_list'][i]
              return users
      return ({})


@app.route('/')
def hello_world():
    return 'Hello, World!'


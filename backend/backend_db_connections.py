from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
import db_connect
from model_mongodb import Song, User, Inventory

db_client = db_connect.get_db_client()

backend = Flask(__name__)
CORS(backend)


@backend.route('/songs', methods=['GET'])
def get_songs():
    if request.method == 'GET':

        search_id = request.args.get('id')
        search_title = request.args.get('title')
        search_artist = request.args.get('artist')
        search_genre = request.args.get('genre')

        if search_id:
            return Song(db_client).find_by_id(int(search_id))

        elif search_title:
            return Song(db_client).find_by_title(search_title)

        elif search_artist:
            return Song(db_client).find_by_artist(search_artist)

        elif search_genre:
            return Song(db_client).find_by_genre(search_genre)

        else:
            return Song(db_client).find_all()


@backend.route('/songs/<id>', methods=['GET'])
def get_song(id):
    if request.method == 'GET':
        return Song(db_client).find_by_id(int(id))['songs'][0]


@backend.route('/users', methods=['GET', 'POST'])
def get_users():
    if request.method == 'GET':

        search_id = request.args.get('id')
        search_name = request.args.get('name')

        if search_id:
            return User(db_client).find_by_id(int(search_id))

        elif search_name:
            return User(db_client).find_by_name(search_name)

        else:
            return User(db_client).find_all()

    elif request.method == 'POST':
        user_to_add = User(request.get_json())

        db_resp = user_to_add.save(db_client)

        http_resp = jsonify(user_to_add, 201)

        return http_resp


@backend.route('/users/<id>', methods=['GET', 'DELETE'])
def get_user(id):
    if request.method == 'GET':
        return User(db_client).find_by_id(int(id))

    elif request.method == 'DELETE':
        user = User({'_id': id})
        db_resp = user.remove(db_client)

        print(db_resp)

        if db_resp['n'] == 1:
            http_resp = jsonify(succes=True, status_code=204)

            return http_resp

        else:
            return jsonify(success=False, status_code=404)


@backend.route('/users/<id>/inv', methods=['GET', 'POST', 'DELETE'])
def get_user_inv(id):
    if request.method == 'GET':

        search_id = request.args.get('id')

        if search_id:
            return Inventory(db_client).find_by_id(int(search_id))

        else:
            return Inventory(db_client).find_all(db_client)
    elif request.method == 'POST':
        inv_to_add = User(request.get_json())

        db_resp = inv_to_add.save(db_client)

        http_resp = jsonify(inv_to_add, 201)

        return http_resp

    elif request.method == 'DELETE':
        inv = Inventory({'_id': id})
        db_resp = inv.remove(db_client)

        print(db_resp)

        if db_resp['n'] == 1:
            http_resp = jsonify(succes=True, status_code=204)

            return http_resp

        else:
            return jsonify(success=False, status_code=404)

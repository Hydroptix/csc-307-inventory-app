import json

import pymongo
import re
from pymongo import IndexModel
from pymongo import TEXT

from bson.objectid import ObjectId


# Modified from bcdasilva's pymongo model


class Model(dict):
    """
    A simple model that wraps mongodb document
    """
    __getattr__ = dict.get
    __delattr__ = dict.__delitem__
    __setattr__ = dict.__setitem__

    def save(self, db_client):
        print(type(self))
        print(type(db_client))
        collection = db_client['inventoryapp'].get_collection(self.type)
        print(f"_id: {self._id}, name: {self.name}")
        data = self.json
        if "_id" not in data:

            data["_id"] = self.get_next_id()
            print(data)
            collection.insert(self.json)
        else:
            collection.update(
                {"_id": int(self._id)})
        self._id = str(self._id)

    def reload(self, id, db_client):
        result = self.collection.find_one({"_id": int(id)})
        print(self.json)
        print(result)
        if result:
            self.collection.update_one({"_id": int(id)}, {'$set': {self.type: self.json}})
            return True
        return False

    def remove(self, db_client, id):
        if id:
            collection = db_client["inventoryapp"].get_collection(self.type)
            resp = collection.remove({"_id": int(id)})
            self.clear()
            return resp


class Song(Model):

    def __init__(self, db_client):

        self.db_client = db_client
        self.collection = db_client["inventoryapp"]["items"]
        self.type = 'items'

        super().__init__()

    def find_all(self):

        songs = {'songs': list(self.collection.find())}
        for song in songs['songs']:
            song["_id"] = str(song["_id"])
        return songs

    def find_by_id(self, id):

        song = self.collection.find({"_id": id})[0]

        return song

    def find_by_title(self, title):
        reg = re.compile("(" + title + ")", re.IGNORECASE)
        songs = {'songs': list(self.collection.find({"title": {'$regex': reg}}))}
        for song in songs['songs']:
            song["_id"] = str(song["_id"])
        return songs

    def find_by_artist(self, artist):
        reg = re.compile("(" + artist + ")", re.IGNORECASE)
        songs = {'songs': list(self.collection.find({"artist": {"$regex": reg}}))}
        for song in songs['songs']:
            song['_id'] = str(song["_id"])
        return songs

    def find_by_genre(self, genre):
        reg = re.compile("(" + genre + ")", re.IGNORECASE)
        songs = {'songs': list(self.collection.find({"genre": {"$regex": reg}}))}
        for song in songs['songs']:
            song['_id'] = str(song["_id"])
        return songs

    def get_next_id(self):

        songs = {'songs': list(self.collection.find())}

        maxid = 0
        for song in songs['users']:
            if int(song["_id"]) > maxid:
                maxid = int(song["_id"])

        return maxid + 1


class User(Model):

    def __init__(self, db_client, json=None):

        self.db_client = db_client
        self.json = json
        print(db_client)
        print(self.json)
        self.collection = db_client["inventoryapp"]["users"]
        self.type = 'users'

        super().__init__()

    def find_all(self):

        users = {'users': list(self.collection.find())}
        for user in users['users']:
            user['_id'] = str(user['_id'])
        return users

    def find_by_id(self, id):

        users = {'users': list(self.collection.find({"_id": int(id)}))}

        return users

    def find_by_name(self, title):
        reg = re.compile("(" + title + ")", re.IGNORECASE)
        users = {'users': list(self.collection.find({"name": {"$regex": reg}}))}
        for user in users['users']:
            user["_id"] = str(user["_id"])
        return users

    def get_next_id(self):

        users = {'users': list(self.collection.find())}

        maxid = 0
        for user in users['users']:
            if int(user["_id"]) > maxid:
                maxid = int(user["_id"])

        return maxid + 1

    def reload(self, id, db_client):
        result = self.collection.find_one({"_id": int(id)})
        print(self.json)
        print(result)
        if result:
            self.collection.update_one({"_id": int(id)}, {'$set': {"name": self.json['name']}})
            return True
        return False


class Inventory(Model):
    def __init__(self, db_client, json=None):
        self.db_client = db_client
        self.collection = db_client["inventoryapp"]['inventories']
        self.json = json
        self.type = "inventories"

        super().__init__()

    def find_all(self):
        invs = {'inventories': list(self.collection.find({}))}
        return invs

    def find_by_id(self, id):
        inv = self.collection.find({"_id": int(id)})[0]

        return inv

    def get_next_id(self):
        invs = {'inventories': list(self.collection.find())}
        maxid = 0
        for inv in invs['inventories']:
            if int(inv["_id"]) > maxid:
                maxid = int(inv["_id"])
        return maxid + 1

    def reload(self, id, db_client):
        result = self.collection.find_one({"_id": int(id)})
        print(self.json)
        print(result)
        if result:
            self.collection.update_one({"_id": int(id)}, {'$set': {"songs": self.json['songs']}})
            self.collection.update_one({'_id': int(id)}, {'$set': {"title": self.json['title']}})
            return True
        return False

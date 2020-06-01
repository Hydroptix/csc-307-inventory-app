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
        collection = self.get_collection(db_client)
        print(f"_id: {self._id}, name: {self.name}")
        if not self._id:
            self._id = self.get_next_id(db_client)
            collection.insert(self)
        else:
            collection.update(
                {"_id": int(self._id)})
        self._id = str(self._id)

    def reload(self):
        if self._id:
            result = self.collection.find_one({"_id": int(self._id)})
            if result:
                self.update(result)
                self._id = str(self._id)
                return True
        return False

    def remove(self, db_client):
        if self._id:
            print(self._id)
            collection = self.get_collection(db_client)
            resp = collection.remove({"_id": int(self._id)})
            self.clear()
            return resp


class Song(Model):

    def __init__(self, db_client):

        self.db_client = db_client
        self.collection = db_client["inventoryapp"]["items"]

        super().__init__()

    def find_all(self):

        songs = {'songs': list(self.collection.find())}
        for song in songs['songs']:
            song["_id"] = str(song["_id"])
        return songs

    def find_by_id(self, id):

        songs = {'songs': list(self.collection.find({"_id": id}))[0]}

        return songs

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

    def get_next_id(self, db_client):

        songs = {'songs': list(self.collection.find())}

        maxid = 0
        for song in songs['users']:
            if int(song["_id"]) > maxid:
                maxid = int(song["_id"])

        return maxid + 1


class User(Model):

    def __init__(self, db_client):

        self.db_client = db_client
        self.collection = db_client["inventoryapp"]["users"]

        super().__init__()

    def find_all(self):

        users = {'users': list(self.collection.find())}
        for user in users['users']:
            user["_id"] = str(user["_id"])
        return users

    def find_by_id(self, id):

        users = {'users': list(self.collection.find({"_id": id}))[0]}

        return users

    def find_by_name(self, title):
        reg = re.compile("(" + title + ")", re.IGNORECASE)
        users = {'users': list(self.collection.find({"name": {"$regex": reg}}))}
        for user in users['users']:
            user["_id"] = str(user["_id"])
        return users

    def get_next_id(self, db_client):

        users = {'users': list(self.collection.find())}

        maxid = 0
        for user in users['users']:
            if int(user["_id"]) > maxid:
                maxid = int(user["_id"])

        return maxid + 1


class Inventory(Model):
    def __init__(self, db_client):
        self.db_client = db_client
        self.collection = db_client["inventoryapp"]['inventories']

        super().__init__()

    def find_all(self, db_client):
        invs = {'inventories': list(self.collection.find({}))}
        return invs

    def find_by_id(self, id, db_client):
        collection = self.get_collection(db_client)
        invs = {'inventories': list(self.collection.find({"_id": id}))}
        for invs in invs['inventories']:
            invs["_id"] = str(invs["_id"])
        return invs

    def get_next_id(self, db_client):
        collection = self.get_collection(db_client)
        invs = {'inventories': list(self.collection.find())}
        maxid = 0
        for inv in invs['inventories']:
            if int(inv["_id"]) > maxid:
                maxid = int(inv["_id"])
        return maxid + 1

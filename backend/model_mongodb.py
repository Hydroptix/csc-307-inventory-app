import pymongo
from bson import ObjectId


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

        songs = {'songs': list(self.collection.find({"_id": id}))}
        for song in songs['songs']:
            song["_id"] = str(song["_id"])
        return songs

    def find_by_title(self, title):

        songs = {'songs': list(self.collection.find({"title": title}))}
        for song in songs['songs']:
            song["_id"] = str(song["_id"])
        return songs

    def find_by_artist(self, artist):

        songs = {'songs': list(self.collection.find({"artist": artist}))}
        for song in songs['songs']:
            song["_id"] = str(songs["_id"])
        return songs

    def find_by_genre(self, genre):

        songs = {'songs': list(self.collection.find({"artist": genre}))}
        for song in songs['songs']:
            song["_id"] = str(songs["_id"])
        return songs


class User(Model):

    def get_collection(self, db_client):

        return db_client["inventoryapp"]["users"]

    def find_all(self, db_client):

        collection = self.get_collection(db_client)

        users = {'users': list(collection.find())}
        for user in users['users']:
            user["_id"] = str(user["_id"])
        return users

    def find_by_id(self, db_client, id):

        collection = self.get_collection(db_client)

        users = {'users': list(collection.find({"_id": id}))}
        for user in users['users']:
            user["_id"] = str(user["_id"])
        return users

    def find_by_name(self, db_client, title):

        collection = self.get_collection(db_client)

        users = {'songs': list(collection.find({"name": title}))}
        for user in users['users']:
            user["_id"] = str(user["_id"])
        return users

    def get_next_id(self, db_client):

        collection = self.get_collection(db_client)

        users = {'users': list(collection.find())}

        maxid = 0
        for user in users['users']:
            if int(user["_id"]) > maxid:
                maxid = int(user["_id"])

        return maxid + 1


class Playlist(Model):

    def get_collection(self, db_client):

        return db_client["inventoryapp"]["inventories"]

    def find_all(self, db_client):

        collection = self.get_collection(db_client)

        playlists = {'playlists': list(collection.find())}
        for playlist in playlists['playlists']:
            playlist["_id"] = str(playlist["_id"])
        return playlists

    def find_by_id(self, db_client, id):

        collection = self.get_collection(db_client)

        playlists = {'playlists': list(collection.find({"_id": id}))}
        for p in playlisys['playlists']:
            p["_id"] = str(p["_id"])
        return playlists

    def find_by_name(self, db_client, title):

        collection = self.get_collection(db_client)

        playlists = {'playlists': list(collection.find({"title": title}))}
        for p in playlists['playlists']:
            p["_id"] = str(p["_id"])
        return playlists

    def get_next_id(self, db_client):

        collection = self.get_collection(db_client)

        playlists = {'playlists': list(collection.find())}

        maxid = 0
        for p in playlists['playlists']:
            if int(p["_id"]) > maxid:
                maxid = int(p["_id"])

        return maxid + 1


from pymongo.errors import DuplicateKeyError

import db_backend_poc as src
from os import path


# Tests whether the backend can reach the database, but not whether the backend
# can authenticate and read from the database
def test_db_connection():
    assert src.try_db_connection()


# Tests whether the backend can get a default database
def test_get_default_db():
    mongo_client = src.get_db_client()

    mongo_client.get_default_database()

    assert True


# Tests whether the backend can get the inventoryapp database
def test_read_db():
    mongo_client = src.get_db_client()

    inventory_db = mongo_client['inventoryapp']

    assert inventory_db is not None


# Tests whether the backend can get the users collection
def test_read_users():
    mongo_client = src.get_db_client()

    db = mongo_client['inventoryapp']
    users_collection = db['users']

    assert users_collection is not None


# Tests whether the backend can get the items collection
def test_read_items():
    mongo_client = src.get_db_client()

    db = mongo_client['inventoryapp']
    items_collection = db['items']

    assert items_collection is not None


# Tests whether the backend can get the items collection
def test_read_inventories():
    mongo_client = src.get_db_client()

    db = mongo_client['inventoryapp']
    inventories_collection = db['inventories']

    assert inventories_collection is not None


# Tests whether the backend can write to the users collection
def test_write_users():
    mongo_client = src.get_db_client()

    db = mongo_client['inventoryapp']
    users = db['users']

    # the _id field is required, or it will be automatically generated on
    # insertion
    new_user = {"_id": -1,
                "first_name": "John",
                "last_name": "Mark",
                "inventories": [-1]}

    try:
        write_result = users.insert_one(new_user)
        assert write_result.acknowledged
    except DuplicateKeyError:
        pass

    delete_result = users.delete_one(new_user)
    assert delete_result.acknowledged


# Tests whether the backend can write to the items collection
def test_write_items():
    mongo_client = src.get_db_client()

    db = mongo_client['inventoryapp']
    items = db['items']

    # the _id field is required, or it will be automatically generated on
    # insertion
    new_item = {"_id": -1,
                "name": "The Item to End All Items",
                "image_url": "www.-1.com",
                "description": "The item to end all items. It is so item "
                               "that you can't even begin to item how item "
                               "it is."}

    try:
        write_result = items.insert_one(new_item)
        assert write_result.acknowledged
    except DuplicateKeyError:
        pass

    delete_result = items.delete_one(new_item)
    assert delete_result.acknowledged


# Tests whether the backend can write to the inventories collection
def test_write_inventories():
    mongo_client = src.get_db_client()

    db = mongo_client['inventoryapp']
    inventories = db['inventories']

    # the _id field is required, or it will be automatically generated on
    # insertion
    new_inventory = {"_id": -1,
                     "first_name": "John",
                     "last_name": "Mark",
                     "inventories": [-1]}

    try:
        write_result = inventories.insert_one(new_inventory)
        assert write_result.acknowledged
    except DuplicateKeyError:
        pass

    delete_result = inventories.delete_one(new_inventory)
    assert delete_result.acknowledged

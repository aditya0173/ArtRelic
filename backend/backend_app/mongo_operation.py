import pymongo # type: ignore


# insert users
def insert_users(users):

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]


    # Check if the collection exists, and create it if it does not
    if "users" not in db.list_collection_names():
        db.create_collection("users")
        print("Collection 'users' created successfully.")
    else:
        print("Connected to existing collection 'users'.")
    """Inserts an users into the 'users' collection."""

    try:
        db.users.insert_one(users)
        print("users inserted successfully.")
    except pymongo.errors.PyMongoError as e:
        print(f"Error while inserting users: {e}")
    finally:
        client.close()



def insert_location(geo_data):
    """Inserts an users location into the 'users' collection."""

    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]


    # Check if the collection exists, and create it if it does not
    if "users" not in db.list_collection_names():
        db.create_collection("location_info")
        print("Collection 'location' created successfully.")
    else:
        print("Connected to existing collection 'users'.")

    try:
        db.location_info.insert_one(geo_data)
        print("locayion inserted successfully.")
    except pymongo.errors.PyMongoError as e:
        print(f"Error while inserting users: {e}")
    finally:
        client.close()




def get_userss(users_id):                                     # not needed
        
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]

    # Check if the collection exists, and create it if it does not
    if "users" not in db.list_collection_names():
        db.create_collection("artoifact")
        print("Collection 'users' created successfully.")
    else:
        print("Connected to existing collection 'users'.")


    """Returns all userss from the 'users' collection."""   
    try:
        userss = db.users.find({'users_id': users_id},{})
        return userss
    except pymongo.errors.PyMongoError as e:
        print(f"Error while fetching userss: {e}")
        return None
    finally:
        client.close()



    
def delete_users(users_id):                                   # not needed
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]

    # Check if the collection exists, and create it if it does not
    if "users" not in db.list_collection_names():
        db.create_collection("artoifact")
        print("Collection 'users' created successfully.")
    else:
        print("Connected to existing collection 'users'.")

    """Deletes an users from the 'users' collection."""
    try:
        db.users.delete_one({'users_id': users_id})
        print("users deleted successfully.")
    except pymongo.errors.PyMongoError as e:
        print(f"Error while deleting users: {e}")
    finally:
        client.close()
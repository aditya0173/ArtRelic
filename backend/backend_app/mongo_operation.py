import pymongo

# Create & Insert Users
def insert_users(users):
    """Inserts a user into the 'users' collection."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]

    if "users" not in db.list_collection_names():
        db.create_collection("users")
        print("Collection 'users' created successfully.")
    else:
        print("Connected to existing collection 'users'.")

    try:
        db.users.insert_one(users)
        print("User inserted successfully.")
    except pymongo.errors.PyMongoError as e:
        print(f"Error while inserting user: {e}")
    finally:
        client.close()


# Create & Insert Location
def insert_location(geo_data):
    """Inserts location data into the 'location_info' collection."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]

    if "location_info" not in db.list_collection_names():
        db.create_collection("location_info")
        print("Collection 'location_info' created successfully.")
    else:
        print("Connected to existing collection 'location_info'.")

    try:
        db.location_info.insert_one(geo_data)
        print("Location inserted successfully.")
    except pymongo.errors.PyMongoError as e:
        print(f"Error while inserting location: {e}")
    finally:
        client.close()


# Get Users Id
def get_user_by_id(users_id):
    """Returns a user from the 'users' collection by user_id."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]

    try:
        user = db.users.find_one({'users_id': users_id})
        return user
    except pymongo.errors.PyMongoError as e:
        print(f"Error while fetching user: {e}")
        return None
    finally:
        client.close()


# Update/Delete Users
def delete_user(users_id):
    """Deletes a user from the 'users' collection."""
    client = pymongo.MongoClient("mongodb://localhost:27017/")
    db = client["relic"]

    try:
        result = db.users.delete_one({'users_id': users_id})
        if result.deleted_count > 0:
            print("User deleted successfully.")
        else:
            print("User not found.")
    except pymongo.errors.PyMongoError as e:
        print(f"Error while deleting user: {e}")
    finally:
        client.close()

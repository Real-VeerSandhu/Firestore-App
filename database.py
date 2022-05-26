from google.cloud import firestore, storage

sr = storage.Client.from_service_account_json("firestore-key.json")

db = firestore.Client.from_service_account_json("firestore-key.json")

def database_info():
    return sr, db

    
import firebase_admin
from firebase_admin import credentials, firestore
import os
from config import load_environment

load_environment()

# https://cave-festival-default-rtdb.firebaseio.com/

firebaseConfig = {
    "apiKey": os.getenv("FIREBASE_API_KEY"),
    "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
    "databaseURL": os.getenv("FIREBASE_DATABASE_URL"),
    "projectId": os.getenv("FIREBASE_PROJECT_ID"),
    "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
    "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
    "appId": os.getenv("FIREBASE_APP_ID"),
    "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
}

cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS_PATH"))
firebase_admin.initialize_app(cred)
db = firestore.client()

class FirestoreDB:
    @staticmethod
    def add_document(collection: str, data: dict, doc_id: str = None) -> None:
        if doc_id:
            db.collection(collection).document(doc_id).set(data)
        else:
            db.collection(collection).add(data)

    @staticmethod
    def get_documents(collection: str) -> list:
        docs = db.collection(collection).stream()
        return [doc.to_dict() for doc in docs]

    @staticmethod
    def delete_document(collection: str, doc_id: str) -> None:
        db.collection(collection).document(doc_id).delete()
        
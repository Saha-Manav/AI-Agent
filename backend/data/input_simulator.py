from pymongo import MongoClient
import datetime
import uuid
from urllib.parse import quote_plus

def get_user_input():
    user = "ManavSaha"
    password = input(" Enter your MongoDB Password: ")
    encoded_password = quote_plus(password)
    cluster = "Cluster0"
    db_name = "dt_agent"

    MONGO_URI = f"mongodb+srv://ManavSaha:{encoded_password}@cluster0.rvtkirc.mongodb.net/dt_agent?retryWrites=true&w=majority"
    client = MongoClient(MONGO_URI)
    db = client[db_name]
    inputs = db["inputs"]

    user_input = {
        "reflection": "I'm feeling stuck managing conflicting deadlines.",
        "project_data": {"KPI": "Launch in 2 weeks", "progress": 60},
        "emotion": {"confidence": 0.4, "frustration": 0.8},
        "session_context": {
            "user_id": "u123",
            "screen": "dashboard",
            "role": "PM",
            "journey_stage": "mid",
            "intent": "decision_help"
        }
    }

    payload = {
        "_id": str(uuid.uuid4()),
        "timestamp": datetime.datetime.utcnow(),
        **user_input,
        "status": "raw"
    }

    inputs.insert_one(payload)
    return user_input

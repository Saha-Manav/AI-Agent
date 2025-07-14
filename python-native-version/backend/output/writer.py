from pymongo import MongoClient
import getpass
import datetime
from urllib.parse import quote_plus


def write_output(user_input, results, explanation):
    user = "ManavSaha"
    password = input(" Enter your MongoDB Password: ")
    encoded_password = quote_plus(password)
    cluster = "cluster0"
    db_name = "dt_agent"
    uri = f"mongodb+srv://ManavSaha:{encoded_password}@cluster0.rvtkirc.mongodb.net/dt_agent?retryWrites=true&w=majority"

    client = MongoClient(uri)
    db = client[db_name]
    outputs = db["outputs"]

    record = {
        "session_id": user_input['session_context']['user_id'],
        "timestamp": datetime.datetime.utcnow(),
        "results": results,
        "explanation": explanation
    }

    outputs.insert_one(record)

import json
import os

from config import DATA_FILE

def load():
    defaults = {
        "users": [],
        "groups": [],
        "anime": {},
        "premium": [],
        "referrals": {},
        "daily": {},
        "coins": {}
    }
    
    if not os.path.exists(DATA_FILE):
        return defaults

    with open(DATA_FILE, "r") as f:
        try:
            data = json.load(f)
        except:
            data = {}

    for key in defaults:
        if key not in data:
            data[key] = defaults[key]
            
    return data

def save(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)
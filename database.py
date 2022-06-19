import toml 
import os
from pathlib import Path
import os


credentials = toml.load(Path("credentials.toml"))
id_= credentials['program_credentials']

srv = id_['mongodb_srv']
def save_history():
    try:
        from pymongo import MongoClient
        client = MongoClient(srv)
        db = client.sktchy
        return db
        # db.history.insert_one(data)

    except Exception as e:
        print(e)






# lol, this is a comment about pushing to github with a token in the file.
# git filter-branch --index-filter "git rm -rf --cached --ignore-unmatch database.py" HEAD

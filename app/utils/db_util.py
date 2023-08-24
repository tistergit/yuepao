from tinydb import TinyDB, Query
import config as config

db = TinyDB(config.DB_FILE)


class DB:
    def addRow(self):
        db.insert({'int': 1, 'char': 'a'})
        db.insert({'int': 1, 'char': 'b'})


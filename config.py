import os

WX_APP_ID = "wx0632ba2512f627fd"

# WX_APP_SECRET = "6bf2e79194041c5c7bd2b06d9bb29e51"

WX_APP_SECRET = os.environ.get("WX_APP_SECRET")

DB_FILE = 'logs/db.json'
import os

from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = str(os.getenv("BOT_TOKEN"))

dirname = os.path.split(os.path.dirname(__file__))[0]
db = 'DataBase\dict.db'
database_name = os.path.join(dirname, db)

admins = [
    os.getenv("ADMIN_ID"),
]



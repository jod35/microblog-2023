from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY") or "you will never get this"
    SQLALCHEMY_DATABASE_URI = os.getenv("DBASE_URL") or "sqlite:///site.db"

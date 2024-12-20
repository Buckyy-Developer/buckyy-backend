from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

# ---------------- CONFIG ENVIRONEMENT VARIABLE ------------#
import os, sys
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(BASE_DIR, ".env"))
sys.path.append(BASE_DIR)
#------------------------------------------------------------#


try:
    SQLALCHEMY_DATABASE_URL = os.environ["DATABASE_URL"]
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
except KeyError:
    print("Environment variable for DATABASE not exist : using SQLLite")
    SQLALCHEMY_DATABASE_URL = "sqlite:///../sql_app.db"
    engine = create_engine(
        SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},
        #echo=True
    )

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
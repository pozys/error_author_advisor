import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app_settings import get_settings as settings

server = settings('MARIA_DB_ADDR')
user = settings('MARIADB_USER')
psw = settings('MARIADB_PASSWORD')
database = settings('MARIADB_DATABASE')

engine = create_engine(f"mariadb+pymysql://{user}:{psw}@{server}:3306/{database}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app_settings import get_settings as settings

server = settings('MARIA_DB_ADDR')

user = settings('MARIADB_USER')
if not user:
    print('MARIADB_USER')
    # raise errors.EnvError()

psw = settings('MARIADB_PASSWORD')
if not psw:
    print('MARIADB_PASSWORD')
    # raise errors.EnvError('MARIADB_PASSWORD')

database = settings('MARIADB_DATABASE')
if not database:
    print('MARIADB_DATABASE')
    # raise errors.EnvError('MARIADB_DATABASE')

print('user', user, 'psw', psw, 'server', server, 'database', database)
engine = create_engine(f"mariadb+pymysql://{user}:{psw}@{server}:3306/{database}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


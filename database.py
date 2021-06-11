import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import errors

server = os.environ.get('MARIA_DB_ADDR')
if not server:
    server = '192.168.120.96'

user = os.environ.get('MARIADB_USER')
if not user:
    raise errors.EnvError('MARIADB_USER')

psw = os.environ.get('MARIADB_PASSWORD')
if not psw:
    raise errors.EnvError('MARIADB_PASSWORD')

database = os.environ.get('MARIADB_DATABASE')
if not database:
    raise errors.EnvError('MARIADB_DATABASE')

engine = create_engine(f"mariadb+pymysql://{user}:{psw}@{server}:3306/{database}")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


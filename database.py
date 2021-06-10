import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

server = os.environ.get('MARIA_DB_ADDR')
if not server:
    server = '192.168.120.96'

print(server)
engine = create_engine(f"mariadb+pymysql://root:root@{server}:3306/error_author_advisor")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


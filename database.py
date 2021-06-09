from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

from sqlalchemy.ext.declarative import declarative_base
import database
import schemas
import models

engine = create_engine("mariadb+pymysql://root:root@192.168.120.96:3306/error_author_advisor")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_user(db: Session):
    return db.query(models.History).first()

def save_report(report, db: Session):
    for item in report:
        history_item = save_report_item(item, db)
        return history_item

def save_report_item(item: schemas.HistoryReportItem, db: Session):
    history_item = database.History(version=item.version, date=item.date, user=item.user, changed_data=item.changed_data)
    db.add(history_item)
    db.commit()
    db.refresh(history_item)

    return history_item

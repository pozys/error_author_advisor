from datetime import datetime, date
from typing import List
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

import conf_storage_history_handler as history_handler
import error_author_handler
import model_training as mt
import data_processing
import predictions

import database
from database import SessionLocal, engine
import schemas

database.Base.metadata.create_all(bind=engine)

app = FastAPI()

class ErrorAuthorRequest(BaseModel):
     metadata: List[str]
     date: datetime = date.today()

def get_db():
    db = SessionLocal()
    try:
         yield db
    finally:
         db.close()

@app.get('/')
async def echo():
     return {"status": "Ok"}

@app.post('/history_report')
async def handle_history_report(report: List[schemas.HistoryReportItem], db: Session = Depends(get_db)):
     history_handler.save_report(report, db)

     return {"status": "Ok"}

@app.get('/history_report/last_version', response_model=schemas.HistoryReportItem)
async def get_last_storage_version(db: Session = Depends(get_db)):
     last_version = history_handler.get_last_storage_version(db)
     
     if last_version is None:
          last_version = schemas.HistoryReportItem()
     
     return last_version

@app.post('/error_author')
async def get_error_author(request_data: ErrorAuthorRequest):
     if not request_data.metadata:
          return ''

     metadata = error_author_handler.get_metadata_from_raw_data(request_data.metadata)
     
     df_expanded = history_handler.df_expanded(metadata, request_data.date)
     
     if df_expanded is None:
          return ''
     elif len(df_expanded) == 1:
          return df_expanded.index[0]
        
     model = mt.trained_model(df_expanded)

     if not metadata:
          return ''

     df_test = data_processing.get_test_dataframe(metadata, df_expanded)

     result = predictions.error_author_prediction(model, df_test)

     return result



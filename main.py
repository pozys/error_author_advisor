from datetime import datetime, date
import time
from typing import List
from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import conf_storage_history_handler as history_handler
import error_author_handler
import model_training as mt
import data_processing
import predictions

class HistoryReportItem(BaseModel):
     version: int = 0
     date: datetime = datetime(1, 1, 1)
     user: str = ''
     changed_data: str = ''

class ErrorAuthorRequest(BaseModel):
     metadata: List[str]
     date: datetime = date.today()

app = FastAPI()
@app.get('/')
async def get_result():
     return {"message": "Hello World"}

@app.post('/test', response_class=JSONResponse)
async def test(metadata: List[str]):     
     return error_author_handler.get_metadata_from_raw_data(metadata)

@app.post('/history_report')
async def handle_history_report(report: List[HistoryReportItem]):
     history_handler.save_report(report)

     return {"status": "Ok"}

@app.get('/history_report/last_version', response_model=HistoryReportItem)
async def get_last_storage_version():
     last_version = history_handler.get_last_storage_version()
     if last_version is None:
          last_version = HistoryReportItem()
     
     return HistoryReportItem.parse_obj(last_version)

@app.post('/error_author')
async def get_error_author(request_data: ErrorAuthorRequest):
     if not request_data.metadata:
          return ''
     t0 = time.time()
     df_expanded = history_handler.df_expanded(request_data.date)
     t1 = time.time() - t0
     print("Time elapsed on df_expanded: ", t1)

     if df_expanded is None:
          return ''
          
     t0 = time.time()
     model = mt.trained_model(df_expanded)
     t1 = time.time() - t0
     print("Time elapsed on trained_model: ", t1)

     t0 = time.time()
     metadata = error_author_handler.get_metadata_from_raw_data(request_data.metadata)
     t1 = time.time() - t0
     print("Time elapsed on get_metadata_from_raw_data: ", t1)

     if not metadata:
          return ''

     t0 = time.time()
     df_test = data_processing.get_test_dataframe(metadata, df_expanded)
     t1 = time.time() - t0
     print("Time elapsed on get_test_dataframe: ", t1)

     t0 = time.time()
     result = predictions.error_author_prediction(model, df_test)
     t1 = time.time() - t0
     print("Time elapsed on error_author_prediction: ", t1)

     return result
from datetime import datetime
from typing import List
from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

import conf_storage_history_handler as history_handler
import model_training as mt
import data_processing
import predictions

class HistoryReportItem(BaseModel):
     version: int = 0
     date: datetime = datetime(1, 1, 1)
     user: str = ''
     changed_data: str = ''

app = FastAPI()
@app.get('/')
async def get_result():
     return {"message": "Hello World"}

@app.post('/history_report')
async def handle_history_report(report: List[HistoryReportItem]):
     history_handler.save_report(report)
     # df = history_handler.df_expanded()
     return {"status": "Ok"}

@app.get('/history_report/last_version', response_model=HistoryReportItem)
async def get_last_storage_version():
     last_version = history_handler.get_last_storage_version()
     if last_version is None:
          last_version = HistoryReportItem()
     
     return HistoryReportItem.parse_obj(last_version)

@app.get('/error_author')
async def get_error_author(metadata: str):
     df_expanded = history_handler.df_expanded()

     if df_expanded is None:
          return ''
          
     model = mt.trained_model(df_expanded)
     df_test = data_processing.get_test_dataframe(metadata, df_expanded)

     return predictions.error_author_prediction(model, df_test)
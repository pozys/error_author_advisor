from pydantic import BaseModel
from datetime import datetime

class HistoryReportItem(BaseModel):
     version: int = 0
     date: datetime = datetime(1, 1, 1)
     user: str = ''
     changed_data: str = ''

     class Config:
        orm_mode = True
from typing import List
import uvicorn
from fastapi import FastAPI, Path, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

class HistoryReport(BaseModel):
     date: str
     user: str
     changed_data: str

app = FastAPI()
@app.get('/')
async def get_result():
     return {"message": "Hello World"}

@app.post('/history_report/')
async def hgandle_history_report(report: List[HistoryReport]):
     return {"message": "Hello World"}

if __name__ == "__main__":
     uvicorn.run('main:app', host="192.168.56.104", port=8080, reload=True)
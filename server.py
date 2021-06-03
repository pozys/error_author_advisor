import uvicorn

if __name__ == "__main__":
     uvicorn.run('main:app', host="192.168.56.104", port=8080, reload=True)
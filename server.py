import os
import uvicorn

if __name__ == "__main__":
     host = os.environ.get('CONTAINER_HOST')

     if not host:
          host = "0.0.0.0"

     uvicorn.run('main:app', host=host, port=8080, reload=True)
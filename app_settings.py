import os
from dotenv import load_dotenv

load_dotenv()

def get_settings(name):
    return os.environ.get(name)

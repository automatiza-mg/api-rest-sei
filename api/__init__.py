from dotenv import load_dotenv
import os
from suds.client import Client
from fastapi import APIRouter
from suds import WebFault

load_dotenv()

token = os.getenv('TOKEN_SEI')
url = os.getenv('URL_SEI')
client = Client(url, faults=False)

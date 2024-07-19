import os
from dotenv import load_dotenv

load_dotenv()

GEOCODER_API_KEY = os.getenv("GEOCODER_API_KEY")
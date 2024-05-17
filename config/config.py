from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file

class Config:
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
    GOOGLE_MAPS_API_KEY = os.getenv('GOOGLE_MAPS_API_KEY')
    WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

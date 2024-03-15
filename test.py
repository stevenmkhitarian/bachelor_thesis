import openai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.environ.get("OPENAI_API_KEY")
openai.api_key=API_KEY # key associated with openai API: sending request to our profile

response = openai.chat

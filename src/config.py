from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
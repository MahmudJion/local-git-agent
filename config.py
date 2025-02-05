import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Default base directory for repositories (optional)
BASE_REPO_PATH = os.getenv("BASE_REPO_PATH", os.getcwd())

import os
import pytest
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """Base URL for the calculator API, loaded from environment variable BASE_URL."""
    url = os.getenv("BASE_URL")
    if not url:
        raise ValueError("Environment variable BASE_URL is not set. Please define it in .env file.")
    return url

import os
import pytest
from dotenv import load_dotenv

# Загружаем переменные из .env
load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    """URL берётся из переменной окружения BASE_URL."""
    url = os.getenv("BASE_URL")
    if not url:
        raise ValueError("Переменная окружения BASE_URL не задана. ")
    return url

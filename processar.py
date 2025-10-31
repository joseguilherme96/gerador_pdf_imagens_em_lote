from src import app
from src.logging_config import setup_logging
import logging
from dynaconf import settings

setup_logging()
app.main()

    
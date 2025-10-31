import logging
from dynaconf import settings

def setup_logging():
    level = logging.DEBUG if settings.DEBUG else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    logging.info(f"Ambiente: {settings.current_env}")
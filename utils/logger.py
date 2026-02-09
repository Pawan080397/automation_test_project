import logging
import os
from datetime import datetime
from logging import Logger

# project root
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(
    LOG_DIR, f"automation_{datetime.now().strftime('%Y%m%d')}.log"
)

def get_logger(name: object) -> Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # file handler
        file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
        file_formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
        )
        file_handler.setFormatter(file_formatter)

        # console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter(
            "%(levelname)s | %(message)s"
        )
        console_handler.setFormatter(console_formatter)

        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

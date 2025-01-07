# Imports to config loging with timestamps
import logging
from uvicorn.config import LOGGING_CONFIG

# Configure log format to include timestamps
LOGGING_CONFIG["formatters"]["default"] = {
    "()": "logging.Formatter",
    "fmt": "%(asctime)s - %(levelname)s - %(message)s",
    "datefmt": "%Y-%m-%d %H:%M:%S",
}

logging.config.dictConfig(LOGGING_CONFIG)


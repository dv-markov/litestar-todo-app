# Настройка логов
import logging
from uvicorn.config import LOGGING_CONFIG
from colorama import Fore, Style, init


# Initialize colorama for cross-platform color support
init(autoreset=True)

# Define color codes for log levels
LOG_LEVEL_COLORS = {
    "INFO": Fore.GREEN,
    "WARNING": Fore.LIGHTYELLOW_EX,
    "ERROR": Fore.RED,
    "DEBUG": Fore.CYAN,
    "CRITICAL": Fore.MAGENTA,
}


class ColorFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        log_level_color = LOG_LEVEL_COLORS.get(record.levelname, "")
        log_level = f"{log_level_color}{record.levelname}{Style.RESET_ALL}"
        message = f"{log_level_color}{record.getMessage()}{Style.RESET_ALL}"
        formatted = f"{self.formatTime(record, self.datefmt)} - {log_level} - {message}"
        return formatted


# Add a separate formatter for access logs
class AccessLogFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        formatted = f"{self.formatTime(record, self.datefmt)} - {record.getMessage()}"
        return formatted


# Update the logging configuration
LOGGING_CONFIG["formatters"]["default"] = {
    "()": ColorFormatter,
    "datefmt": "%Y-%m-%d %H:%M:%S",
}

LOGGING_CONFIG["formatters"]["access"] = {
    "()": AccessLogFormatter,
    "datefmt": "%Y-%m-%d %H:%M:%S",
}

LOGGING_CONFIG["handlers"]["access"]["formatter"] = "access"

logging.config.dictConfig(LOGGING_CONFIG)


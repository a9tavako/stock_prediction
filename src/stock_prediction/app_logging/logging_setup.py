import logging
from logging.handlers import RotatingFileHandler

LOG_FILE_NAME = "flask_app.log"
LOGGING_SIZE_IN_BYTES = 20000
LOGGING_BACKUP = 2

def setup_logging(app):
    logging.basicConfig(level=logging.INFO)  # Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)

    # Add a file handler if you want to log to a file
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes = LOGGING_SIZE_IN_BYTES, backupCount = LOGGING_BACKUP)
    file_handler.setLevel(logging.INFO)

    # Create a log formatter
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    file_handler.setFormatter(formatter)

    # Add the file handler to the Flask app's logger
    app.logger.addHandler(file_handler)
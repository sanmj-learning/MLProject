"""
logging_config.py
A reusable logging configuration module for Python applications.
"""

import logging                      # Core Python logging library
from logging.handlers import RotatingFileHandler  # Handles log file rotation
import os                           # For working with file paths

# -------------------------------------------------------------------
# Function: setup_logging()
# Purpose:  Configure logging settings for the entire application.
# -------------------------------------------------------------------
def setup_logging(log_level=logging.INFO,log_file="app.log",max_bytes=5_000_000,backup_count=5
):
    """
    Sets up logging with console output and rotating log file support.
    """

    # ---------------------------------------------------------------
    # Create logs directory if it doesn't exist
    # This helps keep log files organized.
    # ---------------------------------------------------------------
    logs_dir = "logs"
    os.makedirs(logs_dir, exist_ok=True)

    # Full path of log file inside the logs directory
    log_path = os.path.join(logs_dir, log_file)

    # ---------------------------------------------------------------
    # Define the log message format
    # Example:
    # 2025-01-02 12:34:56,789 - module_name - INFO - This is a log message
    # ---------------------------------------------------------------
    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    date_format = "%Y-%m-%d %H:%M:%S"

    # ---------------------------------------------------------------
    # Set up the root logger (the base logger used by all modules)
    # ---------------------------------------------------------------
    logging.basicConfig(
        level=log_level,            # Set minimum log level (INFO by default)
        format=log_format,          # Log message structure
        datefmt=date_format,        # Datetime formatting
        handlers=[                  # Multiple logging outputs:
            logging.StreamHandler(),  # → Logs printed to the console
            RotatingFileHandler(      # → Logs written to a rotating file
                log_path,
                maxBytes=max_bytes,   # Rotate when file reaches 5MB
                backupCount=backup_count,  # Keep 5 old log files
                encoding="utf-8"       # Avoid encoding issues
            )
        ]
    )

    # Inform the user that logging has been initialized (console only)
    logging.getLogger(__name__).info("Logging initialized successfully.")


# -------------------------------------------------------------------
# Function: get_logger()
# Purpose:  Return a logger instance for a specific module or file.
# -------------------------------------------------------------------
def get_logger(name: str) -> logging.Logger:
    """
    Returns a logger object for the given module.
    Example usage:
        logger = get_logger(__name__)
    """
    return logging.getLogger(name)


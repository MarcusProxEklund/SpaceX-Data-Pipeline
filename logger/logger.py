import logging

# Configure the logging
logging.basicConfig(
    level=logging.INFO,  # Set the logging level
    format='[%(asctime)s][%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("logger/spacex_log.log"), # Log to a file
        logging.StreamHandler()  # Also log to the console
    ]
)

# Create a logger object
logger = logging.getLogger(__name__)
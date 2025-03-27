import logging

# Creating a logger
logger = logging.getLogger('school_logger')
logger.setLevel(logging.DEBUG)

# Creating a handler for the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Defining a common format for messages
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Adding handlers to the logger
logger.addHandler(console_handler)

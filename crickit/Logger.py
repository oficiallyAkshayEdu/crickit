import logging

# Create a logger object.
logger = logging.getLogger(__name__)



handler = logging.StreamHandler()
formatter = logging.Formatter('%(filename)s (%(lineno)d) | %(levelname)s --> %(funcName)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


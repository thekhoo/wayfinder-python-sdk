import logging

def configure_logger():

    logging.basicConfig(
        format="%(levelname)s %(asctime)s.%(msecs)dZ %(name)s %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
        level=logging.INFO,
    )

def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel("INFO")
    return logger


import logging
from logging import config


def logging_conf(logger_name, filename="logging.conf"):
    """
    Initialises logging config and path to logging conf file.
    This function can be initialised at top of every module
    specifying the name of the logger to use
    Parameters
    ----------
    logger_name:string
    Name of the logger to use depending on the module and
    log levels
    filename:string
    name of the logging.conf file.
    Returns
    -------
    """
    config.fileConfig(filename)
    # set up logging
    logger = logging.getLogger(logger_name)
    return logger

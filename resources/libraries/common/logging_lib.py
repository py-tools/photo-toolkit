# ----------------------------------------------
# Imports
# ----------------------------------------------

import logging


# ----------------------------------------------
# Classes
# ----------------------------------------------

class Logger(object):
    """
    """

    def __init__(self, name):
        """
        """
        # create logger
        self._logger = logging.getLogger(str(name))
        self._logger.setLevel(logging.DEBUG)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        # %(name)-12s: %(levelname)-8s %(message)s
        # %(name)s[ %(levelname)s ]-< %(message)s >
        formatter = logging.Formatter('%(name)-10s: %(levelname)-9s < %(message)s >')

        # add formatter to ch
        ch.setFormatter(formatter)

        # add ch to logger
        self._logger.addHandler(ch)

    def debug(self, message):
        """
        """
        self._logger.debug(message)

    def info(self, message):
        """
        """
        self._logger.info(message)

    def warning(self, message):
        """
        """
        self._logger.warning(message)

    def error(self, message):
        """
        """
        self._logger.error(message)

    def critical(self, message):
        """
        """
        self._logger.critical(message)
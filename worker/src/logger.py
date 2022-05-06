import sys
import logging


def config_logger():
    _LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.DEBUG,
        format=_LOG_FORMAT,
        handlers=[
            logging.FileHandler('log.log'),
            logging.StreamHandler()
        ]
    )

    if sys.argv and 'unittest' in sys.argv[0]:
        logging.disable(logging.ERROR)


config_logger()


class Logger:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = logging.getLogger(__name__)
        return cls._instance

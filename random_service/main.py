import logging
from logging import config
from random import randrange
from time import sleep


MIN_TIMEOUT = 3
MAX_TIMOUT = 15


LOG_CONFIG = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console_handler': {
            'level': "DEBUG",
            'formatter': 'default_formatter',
            'class': 'logging.StreamHandler',
        },
        'file_handler': {
            'level': 'DEBUG',
            'formatter': 'default_formatter',
            'class': 'logging.FileHandler',
            'filename': '/logs/random_service.log',
            'mode': 'a',
        },
    },
    'loggers': {
        '': {
            'handlers': ['console_handler', 'file_handler'],
            'level': "DEBUG",
        }
    },
    'formatters': {
        'default_formatter': {
            'format': '%(asctime)s %(levelname)s %(name)s:%(module)s|%(lineno)s: %(message)s'
        },

    },
}
logging.config.dictConfig(LOG_CONFIG)
logger = logging.getLogger(__name__)


def main():
    print("Random service is running")
    qty = 0
    while(1):
        timeout = randrange(MIN_TIMEOUT, MAX_TIMOUT)
        log_level = randrange(0, 4)
        if log_level == 0:
            logger.debug(f"Sleep for {timeout}")
        elif log_level == 1:
            logger.info(f"Sleep for {timeout}")
        elif log_level == 2:
            logger.warning(f"Sleep for {timeout}")
        else:
            logger.error(f"Sleep for {timeout}")
        sleep(timeout)


if __name__ == "__main__":
    main()

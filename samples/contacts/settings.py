from datetime import date
import os
import logging
import logging.config

__author__ = 'okhylkouskaya'

here = lambda path: os.path.join(os.path.realpath(os.path.dirname(__file__)), path)
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': "[%(asctime)s] %(levelname)s [%(filename)s:%(lineno)s] %(message)s"
        },
    },
    'handlers': {
        'datacomconnect_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': here('/Users/okhylkouskaya/LOG/datacomconnect-%s.log' % date.today().strftime('%Y-%m-%d')),
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },
    'loggers': {
        'datacomconnect': {
            'handlers': ['console', 'datacomconnect_handler'],
            'level': 'DEBUG',
            'propagate': False,
        },
        '': {
            'handlers': ['console', 'datacomconnect_handler'],
            'level': 'WARN',
        }
    }
}

logging.config.dictConfig(LOGGING)

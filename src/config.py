import os
import sys
from collections import defaultdict
from src.logger import Logger


def get_config():

    _config = defaultdict(lambda: False)
    _keys = ['SF_USER', 'SF_PWD', 'SF_TOKEN',
             'MAIL_USER', 'MAIL_PASS']

    for _key in _keys:
        if _key in os.environ.keys():
            _config[_key] = os.getenv(_key)
        else:
            logger = Logger()
            logger.send(f"The key {_key} is not set in environment, exiting...")
            sys.exit(4)

    return _config
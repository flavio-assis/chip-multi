import sys
from simple_salesforce import Salesforce
from src.config import get_config
from src.logger import Logger


def SalesForceConnector():
    try:
        conf = get_config()
        _sf = Salesforce(username=conf['SF_USER'],
                         password=conf['SF_PWD'],
                         security_token=conf['SF_TOKEN'])

    except Exception as error:
        logger = Logger()
        logger.send(f"It was not possible to generate a connection with SalesForce! Error: {error}")
        sys.exit(7)

    return _sf
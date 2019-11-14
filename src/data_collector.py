import sys
import pandas as pd
from src.sf_connector import SalesForceConnector
from src.logger import Logger


def get_data() -> pd.DataFrame:
    sf = SalesForceConnector()

    with open('./queries/sf_query.sql', 'r') as file_query:
        sf_query = file_query.read()

    try:
        _df = pd.DataFrame(sf.query_all(sf_query)['records']).drop(columns='attributes')

    except Exception as error:
        logger = Logger()
        logger.send(f"It was not possible to get data from SalesForce! Error: {error}")
        sys.exit(5)

    return _df

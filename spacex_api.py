import pandas as pd

from logger.logger import logger

def get_spacex_data():
    url = 'https://api.spacexdata.com/v4/launches'

    try:
        logger.info("Fetching data from SpaceX API")

        df = pd.read_json(url)
        
        logger.info("Data fetched successfully")

        return df
    
    except Exception as e:
        logger.error(f"An error occurred while fetching data from SpaceX API: {e}", exc_info=True)
        return None
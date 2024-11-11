import requests
import pandas as pd

from logger.logger import logger

def get_spacex_data():
    url = 'https://api.spacexdata.com/v4/launches'

    try:
        logger.info("Fetching data from SpaceX API")

        response = requests.get(url)
        
        if response.status_code != 200:
            logger.error(f"Failed to fetch data from SpaceX API. Status code: {response.status_code}")
            return None
        
        logger.info("Data fetched successfully")

        data = response.json()
        return data
    
    except Exception as e:
        logger.error(f"An error occurred while fetching data from SpaceX API: {e}", exc_info=True)
        return None
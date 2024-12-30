# elasticsearch_client.py

import logging
from elasticsearch import Elasticsearch
from .config import ES_HOST

# Set up logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_es_client():
    try:
        logger.debug(f"Attempting to connect to Elasticsearch at {ES_HOST}")
        es = Elasticsearch(ES_HOST)

        # Use a simple search query to verify connection
        response = es.search(index="_all", body={"query": {"match_all": {}}})
        if response['took'] >= 0:
            logger.info("Successfully connected to Elasticsearch!")
            return es
        else:
            logger.error("Elasticsearch query returned an error response.")
            raise Exception("Elasticsearch connection failed!")

    except Exception as e:
        logger.exception("Error connecting to Elasticsearch:")
        raise e

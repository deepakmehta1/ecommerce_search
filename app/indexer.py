# indexer.py
import json
from elasticsearch.helpers import bulk
from .elasticsearch_client import get_es_client
from .config import ES_INDEX

def index_products(file_path="data/products.json"):
    es = get_es_client()
    
    # Read product data from JSON file
    with open(file_path, 'r') as f:
        products = json.load(f)
    
    # Prepare data for bulk indexing
    actions = [
        {
            "_op_type": "index",
            "_index": ES_INDEX,
            "_id": product['id'],
            "_source": product
        }
        for product in products
    ]
    
    # Bulk index the data
    success, failed = bulk(es, actions)
    print(f"Indexed {success} documents, {failed} failed.")

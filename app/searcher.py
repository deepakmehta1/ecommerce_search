# searcher.py
from .elasticsearch_client import get_es_client
from .config import ES_INDEX

def search_products(query, min_price=None, max_price=None):
    es = get_es_client()
    
    # Construct the query
    body = {
        "query": {
            "bool": {
                "must": [
                    {"match": {"title": query}},
                ],
                "filter": []
            }
        }
    }
    
    if min_price is not None or max_price is not None:
        price_range = {}
        if min_price:
            price_range["gte"] = min_price
        if max_price:
            price_range["lte"] = max_price
        
        body["query"]["bool"]["filter"].append({"range": {"price": price_range}})
    
    response = es.search(index=ES_INDEX, body=body)
    
    print(f"Found {response['hits']['total']['value']} products:")
    for hit in response['hits']['hits']:
        product = hit["_source"]
        print(f"ID: {product['id']} - Title: {product['title']} - Price: {product['price']}")

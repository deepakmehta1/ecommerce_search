# run.py
from app.indexer import index_products
from app.searcher import search_products

def main():
    # First, index the product data
    print("Indexing product data...")
    index_products()
    
    # Then, search for a product
    query = input("Enter a product name to search: ")
    min_price = input("Enter minimum price (leave blank for no filter): ")
    max_price = input("Enter maximum price (leave blank for no filter): ")

    min_price = float(min_price) if min_price else None
    max_price = float(max_price) if max_price else None

    search_products(query, min_price, max_price)

if __name__ == "__main__":
    main()

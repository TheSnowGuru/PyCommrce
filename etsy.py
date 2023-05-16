import requests
import json

ETSY_KEY = 'your_etsy_key'
ETSY_SECRET = 'your_etsy_secret'
SHOP_ID = 'your_shop_id'
PRODUCT_ID = 'listing_id_to_update'

headers = {
    'Content-Type': 'application/json',
    'X-Api-Key': ETSY_KEY
}

url = f"https://openapi.etsy.com/v2/shops/{SHOP_ID}/listings/{PRODUCT_ID}"

data = {
    'title': 'New Title'
}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(response.json())

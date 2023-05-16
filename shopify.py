import requests
import json

API_KEY = 'your_shopify_api_key'
PASSWORD = 'your_shopify_password'
SHOP_NAME = 'your_shop_name'
PRODUCT_ID = 'product_id_to_update'

headers = {
    'Content-Type': 'application/json',
    'X-Shopify-Access-Token': API_KEY
}

url = f"https://{API_KEY}:{PASSWORD}@{SHOP_NAME}.myshopify.com/admin/api/2021-04/products/{PRODUCT_ID}.json"

data = {
    'product': {
        'id': PRODUCT_ID,
        'title': 'New Title'
    }
}

response = requests.put(url, headers=headers, data=json.dumps(data))

print(response.json())

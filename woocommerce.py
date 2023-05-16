from woocommerce import API

wcapi = API(
    url="http://example.com",  # Your store URL
    consumer_key="ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Your consumer key
    consumer_secret="cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",  # Your consumer secret
    wp_api=True,  # Enable the WP REST API integration
    version="wc/v3"  # WooCommerce version
)

data = {
    "product": {
        "name": "New Title"
    }
}

result = wcapi.put("products/PRODUCT_ID", data).json()

print(result)

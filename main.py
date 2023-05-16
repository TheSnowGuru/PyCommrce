from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Now you can access your secrets with os.getenv
shopify_api_key = os.getenv("SHOPIFY_API_KEY")
shopify_password = os.getenv("SHOPIFY_PASSWORD")
shopify_shop_name = os.getenv("SHOPIFY_SHOP_NAME")

etsy_key = os.getenv("ETSY_KEY")
etsy_secret = os.getenv("ETSY_SECRET")
etsy_shop_id = os.getenv("ETSY_SHOP_ID")

woocommerce_url = os.getenv("WOOCOMMERCE_URL")
woocommerce_consumer_key = os.getenv("WOOCOMMERCE_CONSUMER_KEY")
woocommerce_consumer_secret = os.getenv("WOOCOMMERCE_CONSUMER_SECRET")

# Assuming each file has a function named `update_product`
import shopify
import etsy
import woocommerce

PRODUCT_ID = 'your_product_id'

# Update product on Shopify
shopify.update_product(shopify_api_key, shopify_password, shopify_shop_name, PRODUCT_ID, 'New Shopify Title')

# Update product on Etsy
etsy.update_product(etsy_key, etsy_secret, etsy_shop_id, PRODUCT_ID, 'New Etsy Title')

# Update product on WooCommerce
woocommerce.update_product(woocommerce_url, woocommerce_consumer_key, woocommerce_consumer_secret, PRODUCT_ID, 'New WooCommerce Title')

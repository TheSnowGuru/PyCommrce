# PyCommerce

![PyCommerce Logo](logo.png)

Welcome to PyCommerce, your new favorite open-source Python package for managing your e-commerce platforms! With the power of Python, we aim to make the process of managing products across various platforms a breeze.

## Features 🚀

- Unified product management for Shopify, Etsy, and WooCommerce.
- Environment variables for easy configuration.
- Easy-to-use functions for updating your e-commerce product details.
- Open-source and community-driven.

## Getting Started 🏁

Clone the repository and install the requirements:

```bash
git clone [https://github.com/PyCommerce/](https://github.com/TheSnowGuru/PyCommrce/PyCommerce.git)
cd PyCommerce
pip install -r requirements.txt
```

## Setting up .env file 🗄️

Create a .env file in your project root directory and add your platform credentials. See `.env.example` for the format.

Remember, never commit your `.env` file. 

## Usage 🖥️

Import the PyCommerce module and call the update_product function with the relevant parameters for the platform you want to update.

```python
import PyCommerce

PyCommerce.shopify.update_product(api_key, password, shop_name, product_id, new_title)
PyCommerce.etsy.update_product(api_key, secret, shop_id, product_id, new_title)
PyCommerce.woocommerce.update_product(url, consumer_key, consumer_secret, product_id, new_title)
```

## Contributing 👩‍💻👨‍💻

PyCommerce is open-source and we love receiving pull requests! If you have an idea for a feature or want to fix a bug, feel free to make changes and submit a PR. 

Please read our [CONTRIBUTING.md](CONTRIBUTING.md) to get started.

## Jokes 🎭

Why don't programmers like nature? It has too many bugs.

Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25.

## License 📄

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more details.

## Contact 📞

Please raise an issue for any questions or concerns. We'll get back to you faster than you can say 'PyCommerce rocks!'

Join the PyCommerce community and let's revolutionize e-commerce together! 🎉

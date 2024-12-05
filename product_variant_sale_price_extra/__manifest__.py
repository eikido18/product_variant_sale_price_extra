# Copyright 2024 Bojan Anchev <ancevbojan@gmail.com>
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html
{
    "name": "Product Variant Sale Price Extra",
    "summary": "Updates the compare price on the frontend part of Odoo",
    "version": "18.0.1.1.0",
    "category": "Product Management",
    "website": "https://github.com/OCA/product-variant",
    "author": "Bojan Anchev",
    "license": "AGPL-3",
    "installable": True,
    "depends": [
        "website_sale"
    ],
    "data": [
        "views/product_product.xml"
    ],
    "assets": {
        "web.assets_frontend": [
            "product_variant_sale_price_extra/static/src/js/sale_variant_mixin.js"
        ]
    }
}

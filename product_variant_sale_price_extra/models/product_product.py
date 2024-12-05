from odoo import models, fields


class ProductProduct(models.Model):
    _inherit = 'product.product'

    compare_list_price = fields.Monetary(
        string="Compare to Price",
        help="Add a strikethrough price to your shop and product pages for comparison purposes. "
             "It will not be displayed if pricelists apply.",
        currency_field='currency_id',
    )

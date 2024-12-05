from odoo.addons.website_sale.controllers.variant import WebsiteSaleVariantController
from odoo.http import route, request
from odoo import fields


class WebsiteSaleVariantControllerComparePrice(WebsiteSaleVariantController):

    @route()
    def get_combination_info_website(
            self, product_template_id, product_id, combination, add_qty, parent_combination=None,
            **kwargs
    ):
        combination_info = super().get_combination_info_website(
            product_template_id=product_template_id,
            product_id=product_id,
            combination=combination,
            add_qty=add_qty,
            parent_combination=parent_combination,
            **kwargs
        )
        product = request.env['product.product'].browse(combination_info.get('product_id'))
        product_template = product.sudo().product_tmpl_id
        if product_template.product_variant_count == 1:
            compare_list_price = product_template.compare_list_price
        else:
            compare_list_price = product.compare_list_price
        currency_id = request.env.company.currency_id
        to_currency = request.website._get_current_pricelist().currency_id
        if currency_id and to_currency and currency_id != to_currency:
            compare_list_price = currency_id._convert(
                from_amount=compare_list_price,
                to_currency=to_currency,
                company=request.env.company,
                date=fields.Date.today(),
                round=False,
            )
        combination_info.update({
            'has_discounted_price': True,
            'compare_list_price': "{:,.2f}".format(compare_list_price)
        })
        return combination_info

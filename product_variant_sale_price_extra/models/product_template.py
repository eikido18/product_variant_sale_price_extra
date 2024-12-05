from odoo import models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    def _get_combination_info(
            self, combination=False, product_id=False, add_qty=1.0,
            parent_combination=False, only_template=False,
    ):
        response = super()._get_combination_info(
            combination=combination,
            product_id=product_id,
            add_qty=add_qty,
            parent_combination=parent_combination,
            only_template=only_template
        )
        if self and self.product_variant_count == 1 and self.compare_list_price:
            response.update({
                'compare_list_price': self.compare_list_price,
                'has_discounted_price': True
            })
        elif self.product_variant_count > 1:
            compare_list_prices = list(set(self.product_variant_ids.mapped('compare_list_price')) - set([0]))
            if len(compare_list_prices) >= 1:
                response.update({
                    'compare_list_price': compare_list_prices[0],
                    'has_discounted_price': True
                })
        return response

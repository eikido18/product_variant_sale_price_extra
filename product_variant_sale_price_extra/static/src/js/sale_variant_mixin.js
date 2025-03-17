/** @odoo-module **/

import { WebsiteSale } from '@website_sale/js/website_sale';
import VariantMixin from "@website_sale_stock/js/variant_mixin";
import { renderToFragment } from "@web/core/utils/render";
import { markup } from "@odoo/owl";
import publicWidget from "@web/legacy/js/public/public_widget";

const ChangeCombination = VariantMixin._onChangeCombination;
const ChangeCombinationStock = VariantMixin._onChangeCombinationStock;

VariantMixin._onChangeCombinationStock = function (ev, $parent, combination) {
    ChangeCombination.apply(this, arguments);
    ChangeCombinationStock.apply(this, arguments);
    if (combination.has_discounted_price && (combination.compare_list_price || combination.compare_list_price === 0)) {
        var $compare_price = $(".oe_compare_list_price")
        $compare_price.find('.oe_currency_value').html(combination.compare_list_price);
        if (combination.compare_list_price == 0) {
            if (!$compare_price.hasClass('d-none')) {
                $compare_price.addClass('d-none');
            }
        } else {
            if ($compare_price.hasClass('d-none')) {
                $compare_price.removeClass('d-none');
            }
        }
    }
};

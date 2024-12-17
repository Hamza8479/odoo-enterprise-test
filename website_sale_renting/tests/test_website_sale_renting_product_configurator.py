# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import Command
from odoo.tests import tagged
from odoo.tests.common import HttpCase


@tagged('post_install', '-at_install')
class TestWebsiteSaleRentingProductConfigurator(HttpCase):

    def test_website_sale_renting_product_configurator(self):
        self.env.company.write({
            'renting_forbidden_sat': False,
            'renting_forbidden_sun': False
        })
        optional_product = self.env['product.template'].create({
            'name': "Optional product",
            'website_published': True,
            'rent_ok': True,
        })
        main_product = self.env['product.template'].create({
            'name': "Main product",
            'website_published': True,
            'rent_ok': True,
            'optional_product_ids': [Command.set(optional_product.ids)],
        })
        recurrence_3_hours = self.env['sale.temporal.recurrence'].create({
            'duration': 3.0, 'unit': 'hour'
        })
        recurrence_1_day = self.env['sale.temporal.recurrence'].create({
            'duration': 1.0, 'unit': 'day'
        })
        self.env['product.pricing'].create([
            {
                'recurrence_id': recurrence_3_hours.id,
                'product_template_id': main_product.id,
                'price': 5,
            },
            {
                'recurrence_id': recurrence_1_day.id,
                'product_template_id': main_product.id,
                'price': 15,
            },
            {
                'recurrence_id': recurrence_3_hours.id,
                'product_template_id': optional_product.id,
                'price': 6,
            },
            {
                'recurrence_id': recurrence_1_day.id,
                'product_template_id': optional_product.id,
                'price': 16,
            },
        ])
        self.start_tour('/', 'website_sale_renting_product_configurator', login='admin')

# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class motorcycle_stock(models.Model):
#     _name = 'motorcycle_stock.motorcycle_stock'
#     _description = 'motorcycle_stock.motorcycle_stock'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    detailed_type = fields.Selection(
        selection_add=[('motorcycle', 'Motorcycle')],
        ondelete={'motorcycle': 'set product'}
    )

    horsepower = fields.Float('Horsepower')
    top_speed = fields.Float('Top Speed')
    torque = fields.Float('Torque')
    battery_capacity = fields.Selection(
        [('xs', 'Small'), ('0m', 'Medium'), ('0l', 'Large'), ('xl', 'Extra Large')],
        'Battery Capacity'
    )
    charge_time = fields.Float('Charge Time')
    range = fields.Float('Range')
    curb_weight = fields.Float('Curb Weight')
    make = fields.Char('Make')
    model = fields.Char('Model')
    year = fields.Char('Year')

    @api.model
    def _detailed_type_mapping(self):
        type_mapping = super(ProductTemplate, self)._detailed_type_mapping()
        type_mapping['motorcycle'] = 'product'
        return type_mapping

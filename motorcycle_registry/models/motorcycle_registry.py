# -*- coding: utf-8 -*-

from odoo import api, fields, models

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle_registry'
    _description = 'Motorcycle Registry'

    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)

    description = fields.Text()
    level = fields.Selection(string="Level",
                             selection=[
                                 ('beginner', 'Beginner'),
                                 ('intermediate', 'Intermediate'),
                                 ('advanced', 'Advanced'),
                             ],
                             copy=False)

    certificate_title = fields.Binary(string='Binary File')
    current_mileage = fields.Float(string='Current Mileage')
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    license_plate = fields.Char(string="License Plate")
    registry_date = fields.Date(string='Registry Date')
    registry_number = fields.Char(string='Registry Number', required=True)
    vin = fields.Char(string='VIN', required=True)

    owner_id = fields.Many2one(comodel_name='res.partner', ondelete='restrict')
    owner_phone = fields.Char(related='owner_id.phone')
    owner_email = fields.Char(related='owner_id.email')

    make = fields.Char(compute='_compute_from_vin')
    model = fields.Char(compute='_compute_from_vin')


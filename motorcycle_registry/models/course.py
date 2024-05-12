# -*- coding: utf-8 -*-

from odoo import fields, models

class MotorcycleRegistry(models.Model):
    _name = 'motorcycle.registry'
    _description = 'Registro de Motocicletas'
    _rec_name = 'registry_number'

    name = fields.Char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)

    description = fields.Text()
    level = fields.Selection(string="Level",
                             selection=[
                                 ('begginer', 'Begginer'),
                                 ('intermediate', 'Intermediate'),
                                 ('advanced', 'Advanced'),
                             ],
                             copy=False)

    certificate_title = fields.Binary(string='Binary File')
    current_mileage = fields.Float(string='Current Mileage')
    first_name = fields.Char(string="First Name", required=True)
    last_name = fields.Char(string="Last Name", required=True)
    license_platte = fields.Char(string="License Plate")
    registry_date = fields.Date(string='Registry Date')
    registry_number = fields.Char(string='Registry Number', required=True)
    vin = fields.Char(string='VIN', required=True)
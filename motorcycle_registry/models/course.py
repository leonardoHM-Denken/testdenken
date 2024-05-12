# -*- coding: utf-8 -*-

from odoo import fields, models

class Course(models.Model):
    _name = 'motorcycle_registry.course'
    _description = 'Registro de Motocicletas'

    name = fields.char(string="Title", required=True)
    active = fields.Boolean(string="Active", default=True)

    description = fields.Text()
    level = fields.selection(string="Level",
                             selection=[
                                 ('begginer', 'Begginer'),
                                 ('intermediate', 'Intermediate'),
                                 ('advanced', 'Advanced'),
                             ],
                             copy=False)

    certificate_title = fields.binary(string='Binary File')
    current_mileage = fields.float(string='Current Mileage')
    first_name = fields.char(string="First Name", required=True)
    last_name = fields.char(string="Last Name", required=True)
    license_platte = fields.char(string="License Plate")
    registry_date = fields.date(string='Registry Date')
    registry_number = fields.char(string='Registry Number', required=True)
    vin = fields.Char(string='VIN', required=True)
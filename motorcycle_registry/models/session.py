from odoo import api, fields, models

class Session(models.Model):
    _name = 'motorcycle_registry.session'
    _description = 'Session Info'

    name = fields.Char(string="Name", required=True)
    start_date = fields.Date(string="Start Date")
    duration = fields.Float(string="Duration")
    seats = fields.Integer(string="Number of Seats")

    @api.model
    def create(self, vals_list):
        # Aquí, vals_list es una lista de diccionarios.
        # Cada diccionario contiene los valores para crear un nuevo registro.
        # Sobrescribimos el método `create` para manejar múltiples registros a la vez.
        sessions = super(Session, self).create(vals_list)
        # Realiza cualquier procesamiento adicional que necesites aquí.
        return sessions

from odoo import http

class MotorcycleMap(http.Controller):
    @http.route('/motorcycle_map/', auth='public')
    def index(self, **kw):
        return "Hello, world"

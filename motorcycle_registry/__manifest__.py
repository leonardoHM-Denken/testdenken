# -*- coding: utf-8 -*-
{
    'name': "Motorcyle Registry",
    'summary': "Manage Registration Motorcycle",
    'description': """
        Motorcycle Registry
        ===================
        Este módulo es para registrar motos
    """,
    'author': "LHM",
    'website': "www.odoo.com",
    'license': 'OPL-1',
    'category': 'Kawiil/registry',
    'version': '0.1',
    'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'views/motorcycle_registry_menuitems.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'application': True,
}

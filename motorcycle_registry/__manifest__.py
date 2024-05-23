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
        'security/motorcycle_security.xml',
        'data/session_data.xml',
        'views/motorcycle_registry_menuitems.xml',
        'views/motorcycle_registry_views.xml',
        'views/session_views.xml',
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'installable': True,
    'application': True,
}


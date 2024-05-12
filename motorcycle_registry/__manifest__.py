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
    'category': 'Kawiil/registry',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/motorcycle_registry_groups.xml',
        'security/ir.model.access.csv',
        'security/motorcycle_registry_security.xml', 
    ],
    'demo': [
        'demo/course_demo.xml',
    ],
    'application': True,
}

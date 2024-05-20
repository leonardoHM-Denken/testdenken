{
    'author': "LHM",
    'website': "www.odoo.com",
    'license': 'OPL-1',
    'category': 'Kawiil/website',
    'version': '0.1',
    'name': 'Motorcycle Map',   
    'summary': 'Mapa de ubicación de motocicletas',
    'description': 'Muestra un mapa con la ubicación de las motocicletas registradas.',
    'depends': ['motorcycle_registry', 'portal'],
    'data': [
        'security/ir.model.access.csv',
        'security/portal_security.xml',
        'views/motorcycle_templates.xml',
    ],
    'demo': [
        'demo/motorcycle_registry_demo.xml',
    ],
}

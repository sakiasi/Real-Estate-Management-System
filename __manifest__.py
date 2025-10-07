{
    'name': 'Estate',
    'author':'saki',
    'version': '1.2',
    'category': 'Uncategorized',
    'sequence': 1,
    'summary': 'Estate management system',
    'description': "A simple estate management system for managing properties.",
    'website': 'https://slppharmacy.com',
    'depends': [
        'base',
    ],
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
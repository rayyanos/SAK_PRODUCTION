# -*- coding: utf-8 -*-
{
    'name': "POS Use Wise",
    'version': '1.0.0',
    'category': 'Point of Sale',
    'author': 'TL Technology',
    'live_test_url': 'http://posodoo.com/web/signup',
    'price': '0',
    'website': 'http://posodoo.com',
    'sequence': 0,
    'depends': [
        'point_of_sale'
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/parameter_data.xml',
        'template/import_library.xml',
        'views/res_users.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml'
    ],
    'images': ['static/description/icon.png'],
    'support': 'thanhchatvn@gmail.com',
    "license": "OPL-1",
    'installable': True,
    'application': True,
 
}

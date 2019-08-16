{
    'name': 'POS Default Customer Selection(Community & Enterprise)',
    'version': '12.0.4',
    'category': 'Point of Sale',
    'summary': 'POS Default Customer Selection for Order in POS Interface',
    'description': """ POS Default Customer Selection for Order in POS Interface
    """,
    'price': 4,
    'currency': 'EUR',
    'author': 'Kiran Kantesariya',
    'email': 'risingsuntechcs@gmail.com',
    'license': 'OPL-1',
    'depends': ['point_of_sale'],
    # "live_test_url" : "",
    'data': [
        'views/sun_pos_config_views.xml',
        'views/templates_call.xml'
    ],
    'qweb': [
        ],
    'images': ['static/description/main_screenshot.jpg'],
    'demo': [],
    'test': [],
    'installable': True,
    'auto_install': False,
}

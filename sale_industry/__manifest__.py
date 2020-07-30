# -*- coding: utf-8 -*-
{
    'name': "Sale Industry",
    'author': "Eslam Mohamed Rezk",
    'version': '12.0.1.0.0',
    'installable': True,
    'application': True,
    # any module necessary for this one to work correctly
    'depends': ['base','sale','stock'],

    # always loaded
    'data': [
        'views/sale_order.xml',
        'views/inventory.xml',
        # 'views/invoicing.xml',
    ],
}

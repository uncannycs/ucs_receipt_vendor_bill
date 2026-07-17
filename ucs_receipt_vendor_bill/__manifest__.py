# -*- coding: utf-8 -*-
{
    'name': 'Receipt Vendor Bill',
    'version': '19.0.1.0.0',
    'summary': 'Add Vendor Bill column in Receipt transfer',
    'category': 'Inventory/Inventory',
    "website": "https://uncannycs.com",
    "author": "Uncanny Consulting Services LLP",
    "maintainers": "Uncanny Consulting Services LLP",
    'depends': ['stock', 'purchase_stock', 'account'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'images': ['static/description/banner.gif'],
    'license': 'LGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,
    "price": 50,
    "currency": "USD"
}


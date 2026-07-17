# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO Open Source Management Solution
#
#    ODOO Addon module by Uncanny Consulting Services LLP
#    Copyright (C) 2023 Uncanny Consulting Services LLP (<https://uncannycs.com>).
#
##############################################################################
{
    'name': 'Receipt Vendor Bill',
    'summary': 'Add Vendor Bill column in Receipt transfer',
    'version': '19.0.1.0.0',
    'category': 'Inventory/Inventory',
    "website": "https://uncannycs.com",
    "author": "Uncanny Consulting Services LLP",
    "maintainers": "Uncanny Consulting Services LLP",
    "license": "Other proprietary",
    'depends': ['stock', 'purchase_stock', 'account'],
    'data': [
        'views/stock_picking_views.xml',
    ],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}


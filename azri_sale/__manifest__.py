# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Sale Custom',
    'version': '2.0',
    'category': 'sale',
    'sequence': 55,
    'summary': 'Sales Custom',
    'depends': ['sale', 'sale_mrp'],
    'description': "",
    'data': [
        # 'security/mrp_security.xml',
        # 'security/ir.model.access.csv',
        'views/sale_order_views.xml',
    ],
    'qweb': [],
    'demo': [
    
    ],
    'test': [],
    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}

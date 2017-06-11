# -*- coding: utf-8 -*-
{
    'name': "hide_price_website_sale",

    'summary': """
        Remove price from website_sale module""",

    'description': """
        This module extended from eCommerce(website_sale) module and remove price in 2 pages
        1. Product item
        2. Product price
    """,

    'author': "Wittawin Kahuttanaseth",
    'website': "http://www.go-things.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['website_sale'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
}
# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Ceid Indicators',
    'version': '2.0.0',
    # 'category': 'Operations/Helpdesk',
    'category': 'L1ght',
    'summary': 'Track portal sites',
    # 'website': 'https://www.odoo.com/page/helpdesk',
    'depends': [
        'contacts',
    ],
    'description': """
site - portal site Management App
=================================

Features:


    """,
    'data': [
        # 'security/ir.model.access.csv',
        'views/site_views.xml',
    ],
    'application': True,
}

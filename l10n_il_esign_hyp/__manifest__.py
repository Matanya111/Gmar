# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'EDI for Israel',
    'version': '0.1',
    'summary': 'Electronic Invoicing for Israel',
    'category': 'Localization',
'description': """
    """,
    'depends': [
    ],
    "data": [
        'security/ir.model.access.csv',
        'views/l10n_il_edi_certificate_views.xml',
    ],
    'installable': True,
    'application': True,
}

# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'fame_dss',
    'version': '0.1',
    'summary': 'GMAR_project',
    'category': 'Localization',
    'description': """""",
    'depends': [
    ],
    "data": ['security/ir.model.access.csv',
        'views/ceid_list_views.xml',
        'views/project_list_views.xml',
        'views/restrictive_tool_views.xml',
        'views/vf_ceid_views.xml',
        'views/execl_1_views.xml',
        'views/execl_2_views.xml',
        'views/ceid_dashboards.xml'
    ],
    'installable': True,
    'application': True,
}

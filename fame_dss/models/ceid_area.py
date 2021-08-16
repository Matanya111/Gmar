from odoo import _, api, fields, models, tools

class ceid_area(models.Model):
    _name = 'ceid.area'
    _description = 'engineers ceids list'

    name = fields.Char("area Name")
    excel_1_ceid = fields.One2many('execl.1', 'AREA')
from odoo import _, api, fields, models, tools

class execl_1(models.Model):
    _name = 'execl.1'
    _description = 'availability execl'

    AREA = fields.Many2one('ceid.area')
    ceid_list = fields.Many2one('ceid.list', "Ceid")
    MOM = fields.Char()
    CHAMBER = fields.Char()
    WW = fields.Integer()
    AVAILABILITY = fields.Float(group_operator="avg")
    GOAL = fields.Float()
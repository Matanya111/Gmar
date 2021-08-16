from odoo import _, api, fields, models, tools

class execl_eu(models.Model):
    _name = 'execl.eu'
    _description = 'eu availability execl'

    AREA = fields.Char()
    ceid_list_3 = fields.Many2one('ceid.list', "Ceid")
    MOM = fields.Char()
    CHAMBER = fields.Char()
    WW = fields.Integer()
    AVAILABILITY = fields.Float(group_operator="avg")
    GOAL = fields.Float()

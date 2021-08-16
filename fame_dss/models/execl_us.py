from odoo import _, api, fields, models, tools

class execl_us(models.Model):
    _name = 'execl.us'
    _description = 'us availability execl'

    AREA = fields.Char()
    ceid_list_4 = fields.Many2one('ceid.list', "Ceid")
    MOM = fields.Char()
    CHAMBER = fields.Char()
    WW = fields.Integer()
    AVAILABILITY = fields.Float(group_operator="avg")
    GOAL = fields.Float()

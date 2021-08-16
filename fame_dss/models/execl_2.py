from odoo import _, api, fields, models, tools

class execl_2(models.Model):
    _name = 'execl.2'
    _description = 'down time execl'

    AREA = fields.Char()
    ceid_list_2 = fields.Many2one('ceid.list', "Ceid")
    MOM = fields.Char()
    CHAMBER = fields.Char()
    WW = fields.Integer()
    STATUS = fields.Char()
    TIME = fields.Float()

from odoo import _, api, fields, models, tools

class ceid_area(models.Model):
    _name = 'ceid.area'
    _description = 'engineers ceids list'

    name = fields.Char("area Name")
    excel_1_ceid = fields.One2many('execl.1', 'AREA')
    is_verified = fields.Boolean(default=False)

    def action_show_ceid_by_area(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ceid.list',
            'name': 'ceid related to area',
            'view_mode': 'tree,form',
            'target': 'current',
            'domain': [('area', '=', self.name)],
        }

    def action_verify_user(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'verify_user',
            'name': 'verify user',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_area': self.id}
        }

class verify_user(models.TransientModel):
    _name = 'verify_user'
    _description = 'verify user login'

    name = fields.Char('File Name')
    user_name = fields.Char('user Name')
    pass_name = fields.Char('password')
    state = fields.Selection([('choose', 'choose'), ('get', 'get')], default='choose')
    is_allowed = fields.Boolean(default=False)
    area = fields.Many2one('ceid.area')

    def open_area(self):
        self.area.is_verified = True

    def verify(self):
        self.write({'state': 'get', 'is_allowed': True})

        return {
            'type': 'ir.actions.act_window',
            'res_model': 'verify_user',
            'view_mode': 'form',
            'res_id': self.id,
            'views': [(False, 'form')],
            'target': 'new',
        }
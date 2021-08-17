from odoo import _, api, fields, models, tools

class ceid_area(models.Model):
    _name = 'ceid.area'
    _description = 'engineers ceids list'

    name = fields.Char("area Name")
    excel_1_ceid = fields.One2many('execl.1', 'AREA')

    def action_show_ceid_by_area(self):
        # ceid_tree = self.env.ref('fame_dss.ceid_list_tree', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ceid.list',
            'name': 'ceid related to area',
            'view_mode': 'tree,form',
            # 'views': [(ceid_tree.id, 'tree')],
            # 'view_id': ceid_tree.id,
            'target': 'current',
            'domain': [('area', '=', self.name)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    # lists_ceid = fields.One2many('ceid.list', 'area', compute="_get_ceids", store=True)

    # @api.depends('excel_1_ceid')
    # def _get_ceids(self):
    #     chambers = self.excel_1_ceid.search([('AREA', '=', self.id)])
    #     uniqe_ch = []
    #     uniqe_ch_char = []
    #     if chambers:
    #         for c in chambers:
    #             if c['ceid_list'] not in uniqe_ch_char:
    #                 uniqe_ch_char.append(c['ceid_list'])
    #                 uniqe_ch.append(c['ceid_list'].id)
    #     self.lists_ceid = uniqe_ch
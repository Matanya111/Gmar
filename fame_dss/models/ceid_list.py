# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models, tools

class ceid_list(models.Model):
    _name = 'ceid.list'
    _description = 'engineers ceids list'

    name = fields.Char("Ceid Name")
    area = fields.Char()
    ceid_availablity = fields.One2many('execl.1', 'ceid_list')
    ceid_availablity = fields.One2many('execl.2', 'ceid_list_2')



    def action_show_ceid_avail(self):
        avail_graph = self.env.ref('fame_dss.view_ceid_graph_1', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.1',
            'name': 'ceid availability 13 WW',
            'view_mode': 'graph',
            'views': [(avail_graph.id, 'graph')],
            'view_id': avail_graph.id,
            'target': 'new',
            # 'domain': [('id', 'in', self.mrp_ids.ids)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    def action_show_ch_avail(self):
        avail_pivot = self.env.ref('fame_dss.view_ceid_pivot_2', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.1',
            'name': 'ch availability 4 WW',
            'view_mode': 'pivot',
            'views': [(avail_pivot.id, 'pivot')],
            'view_id': avail_pivot.id,
            'target': 'new',
            # 'domain': [('id', 'in', self.mrp_ids.ids)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    def action_show_13_4_avail(self):
        avail_pivot = self.env.ref('fame_dss.view_ceid_pivot_3', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.1',
            'name': 'ceid Availability 13 and 4 WW',
            'view_mode': 'pivot',
            'views': [(avail_pivot.id, 'pivot')],
            'view_id': avail_pivot.id,
            'target': 'new',
            # 'domain': [('id', 'in', self.mrp_ids.ids)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    def action_show_ceid_dt(self):
        avail_pivot = self.env.ref('fame_dss.view_ceid_pivot_4', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.2',
            'name': 'ceid down time pareto',
            'view_mode': 'pivot',
            'views': [(avail_pivot.id, 'pivot')],
            'view_id': avail_pivot.id,
            'target': 'new',
            # 'domain': [('id', 'in', self.mrp_ids.ids)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    def action_show_ch_dt(self):
        avail_pivot = self.env.ref('fame_dss.view_ceid_pivot_5', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.2',
            'name': 'ch down time pareto',
            'view_mode': 'pivot',
            'views': [(avail_pivot.id, 'pivot')],
            'view_id': avail_pivot.id,
            'target': 'new',
            # 'domain': [('id', 'in', self.mrp_ids.ids)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }



#    date_start = fields.Datetime(readonly=True, help="The date on which the certificate starts to be valid")
#    date_end = fields.Datetime(readonly=True, help="The date on which the certificate expires")
#    sig_token = fields.Char()
#
#    def generate_signature(self):
#        print("helllo")


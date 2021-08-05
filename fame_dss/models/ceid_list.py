# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models, tools

class ceid_list(models.Model):
    _name = 'ceid.list'
    _description = 'engineers ceids list'

    name = fields.Char("Ceid Name")
    ceid_avail_1 = fields.One2many('execl.1', 'ceid_list')
    ceid_avail_2 = fields.One2many('execl.2', 'ceid_list_2')
    ceid_avail_3 = fields.One2many('execl.eu', 'ceid_list_3')
    ceid_avail_4 = fields.One2many('execl.us', 'ceid_list_4')
    last_4_weeks_avail = fields.Float(compute='_compute_last_4', store=True)
    last_13_weeks_avail = fields.Float(compute='_compute_last_13', store=True)
    goal = fields.Float(related="ceid_avail_1.GOAL")

    @api.depends('ceid_avail_1')
    def _compute_last_4(self):
        for record in self:
            avails = record.ceid_avail_1.search([('ceid_list', '=', self.id)], order='WW desc')
            latest_week = avails[0]['WW']
            latest_weeks = [latest_week, latest_week - 1, latest_week - 2, latest_week - 3]
            reports = record.ceid_avail_1.search([('WW', 'in', latest_weeks), ('ceid_list', '=', self.id)])
            record.last_4_weeks_avail = sum(report.AVAILABILITY for report in reports) / len(reports)
            print(record.last_4_weeks_avail)

    @api.depends('ceid_avail_1')
    def _compute_last_13(self):
        for record in self:
            avails = record.ceid_avail_1.search([('ceid_list', '=', self.id)], order='WW desc')
            latest_week = avails[0]['WW']
            latest_weeks = [latest_week, latest_week - 1, latest_week - 2, latest_week - 3, latest_week - 4, latest_week - 5, latest_week - 6, latest_week - 7, latest_week - 9, latest_week - 10, latest_week - 11, latest_week - 12]
            reports = record.ceid_avail_1.search([('WW', 'in', latest_weeks), ('ceid_list', '=', self.id)])
            record.last_13_weeks_avail = sum(report.AVAILABILITY for report in reports) / len(reports)
            print(record.last_13_weeks_avail)
            
    def action_show_ceid_avail(self):
        avail_graph = self.env.ref('fame_dss.view_ceid_avail', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.1',
            'name': 'ceid availability 13 WW',
            'view_mode': 'graph',
            'views': [(avail_graph.id, 'graph')],
            'view_id': avail_graph.id,
            'target': 'new',
            'domain': [('ceid_list', '=', self.id)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    def action_show_ch_avail(self):
        avail_graph = self.env.ref('fame_dss.view_ch_avail', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.1',
            'name': 'ch availability 4 WW',
            'view_mode': 'graph',
            'views': [(avail_graph.id, 'graph')],
            'view_id': avail_graph.id,
            'target': 'new',
            'domain': [('ceid_list', '=', self.id)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    def action_show_13_4_avail(self):
        avail_form = self.env.ref('fame_dss.view_4_13_weeks', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'ceid.list',
            'name': 'ch availability 4 WW',
            'view_mode': 'form',
            'views': [(avail_form.id, 'form')],
            'view_id': avail_form.id,
            'target': 'new',
            'res_id': self.id,
        }

    def action_show_ceid_dt(self):
        avail_graph = self.env.ref('fame_dss.view_ceid_dt', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.2',
            'name': 'ceid down time pareto',
            'view_mode': 'graph',
            'views': [(avail_graph.id, 'graph')],
            'view_id': avail_graph.id,
            'target': 'new',
            'domain': [('ceid_list_2', '=', self.id)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }

    def action_show_ch_dt(self):
        avail_graph = self.env.ref('fame_dss.view_ch_dt', raise_if_not_found=False)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.2',
            'name': 'ch down time pareto',
            'view_mode': 'graph',
            'views': [(avail_graph.id, 'graph')],
            'view_id': avail_graph.id,
            'target': 'new',
            'domain': [('ceid_list_2', '=', self.id)],
            # 'context': dict(self._context, create=True, default_stock_id = self.id, default_origin = self.name),
        }


    def action_show_is_ch(self):
        ch_tree = self.env.ref('fame_dss.view_show_is_ch', raise_if_not_found=False)
        chambers = self.ceid_avail_1.search([('ceid_list', '=', self.id)])
        uniqe_ch = []
        uniqe_ch_char = []
        if chambers:
            for c in chambers:
                if c['CHAMBER'] not in uniqe_ch_char:
                    uniqe_ch_char.append(c['CHAMBER'])
                    uniqe_ch.append(c.id)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.1',
            'name': 'ceid is ch',
            'view_mode': 'tree',
            'views': [(ch_tree.id, 'tree')],
            'view_id': ch_tree.id,
            'target': 'new',
            'domain': [('ceid_list', '=', self.id), ('id', 'in', uniqe_ch)],
        }

    def action_show_eu_ch(self):
        ch_tree = self.env.ref('fame_dss.view_show_eu_ch', raise_if_not_found=False)
        chambers = self.ceid_avail_3.search([('ceid_list_3', '=', self.id)])
        uniqe_ch = []
        uniqe_ch_char = []
        if chambers:
            for c in chambers:
                if c['CHAMBER'] not in uniqe_ch_char:
                    uniqe_ch_char.append(c['CHAMBER'])
                    uniqe_ch.append(c.id)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.eu',
            'name': 'ceid eu ch',
            'view_mode': 'tree',
            'views': [(ch_tree.id, 'tree')],
            'view_id': ch_tree.id,
            'target': 'new',
            'domain': [('ceid_list_3', '=', self.id), ('id', 'in', uniqe_ch)],
        }

    def action_show_us_ch(self):
        ch_tree = self.env.ref('fame_dss.view_show_us_ch', raise_if_not_found=False)
        chambers = self.ceid_avail_4.search([('ceid_list_4', '=', self.id)])
        uniqe_ch = []
        uniqe_ch_char = []
        if chambers:
            for c in chambers:
                if c['CHAMBER'] not in uniqe_ch_char:
                    uniqe_ch_char.append(c['CHAMBER'])
                    uniqe_ch.append(c.id)
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'execl.us',
            'name': 'ceid us ch',
            'view_mode': 'tree',
            'views': [(ch_tree.id, 'tree')],
            'view_id': ch_tree.id,
            'target': 'new',
            'domain': [('ceid_list_4', '=', self.id), ('id', 'in', uniqe_ch)],
        }



# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models, tools

class project_list(models.Model):
    _name = 'project.list'
    _description = 'projects monitoring list'

    area = fields.Char()
    ceid = fields.Char()
    project_name = fields.Char()
    project_start_date = fields.Char()
    summary_and_decisions = fields.Char()
    eng = fields.Char()
    last_update = fields.Char()

#    date_start = fields.Datetime(readonly=True, help="The date on which the certificate starts to be valid")
#    date_end = fields.Datetime(readonly=True, help="The date on which the certificate expires")
#    sig_token = fields.Char()
#
#    def generate_signature(self):
#        print("helllo")
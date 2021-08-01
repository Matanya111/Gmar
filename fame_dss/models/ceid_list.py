# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models, tools

class ceid_list(models.Model):
    _name = 'ceid.list'
    _description = 'engineers ceids list'

    name = fields.Char("Ceid Name")
    area = fields.Char()
    ceid_availablity = fields.One2many('execl.1', 'ceid_list')



#    date_start = fields.Datetime(readonly=True, help="The date on which the certificate starts to be valid")
#    date_end = fields.Datetime(readonly=True, help="The date on which the certificate expires")
#    sig_token = fields.Char()
#
#    def generate_signature(self):
#        print("helllo")
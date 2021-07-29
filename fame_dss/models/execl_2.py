# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import _, api, fields, models, tools

class execl_2(models.Model):
    _name = 'execl.2'
    _description = 'down time execl'

    AREA = fields.Char()
    CEID = fields.Char()
    MOM = fields.Char()
    CHAMBER = fields.Char()
    WW = fields.Char()
    STATUS = fields.Char()
    TIME = fields.Char()

#    date_start = fields.Datetime(readonly=True, help="The date on which the certificate starts to be valid")
#    date_end = fields.Datetime(readonly=True, help="The date on which the certificate expires")
#    sig_token = fields.Char()
#
#    def generate_signature(self):
#        print("helllo")
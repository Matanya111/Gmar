# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import datetime
from datetime import time
from dateutil import relativedelta

from odoo import api, fields, models, tools, _
from odoo.exceptions import AccessError


class L1ghtSite(models.Model):
    _name = 'l1ght.site'
    _description = 'Site'

    name = fields.Char(string="Site URL", index=True)
    site_state = fields.Selection(string="Status", selection=[('active','Active'),('inactive','Inactive'),
    ('unreachable','Unreachable')])
    partner_id = fields.Many2one('res.partner', string='Customer')
    address = fields.Char(string = 'IP')
    report_date = fields.Datetime(string = 'Last report date')

    csam = fields.Boolean(string="CSAM", compute="_get_latest_classification", readonly=False, default=False, store=True, tracking=True)
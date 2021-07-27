# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import hashlib
import ssl
from base64 import b64decode, b64encode
from copy import deepcopy
from lxml import etree
from pytz import timezone
from datetime import datetime
from OpenSSL import crypto

from odoo import _, api, fields, models, tools
from odoo.exceptions import ValidationError
import requests


class Certificate(models.Model):
    _name = 'l10n_il_edi.certificate'
    _description = 'Israel Digital Certificate'

    name = fields.Char()
    state = fields.Char()
    country = fields.Char()
    organization = fields.Char()
    domain = fields.Char()
    email = fields.Char()
    password = fields.Char(help="Passphrase for the certificate")

    date_start = fields.Datetime(readonly=True, help="The date on which the certificate starts to be valid")
    date_end = fields.Datetime(readonly=True, help="The date on which the certificate expires")

    sig_token = fields.Char()


    def generate_signature(self):

        print("helllo")
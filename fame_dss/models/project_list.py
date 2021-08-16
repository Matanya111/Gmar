from odoo import _, api, fields, models, tools

class project_list(models.Model):
    _name = 'project.list'
    _description = 'projects monitoring list'

    area = fields.Char()
    ceid = fields.Char()
    project_name = fields.Char()
    project_start_date = fields.Char()
    project_end_date = fields.Char()
    summary_and_decisions = fields.Char()
    eng = fields.Char()
    last_update = fields.Char()

from odoo import _, api, fields, models, tools

class project_list(models.Model):
    _name = 'project.list'
    _description = 'projects monitoring list'

    area = fields.Char()
    ceid = fields.Many2one('ceid.list')
    project_name = fields.Char()
    project_start_date = fields.Datetime()
    project_end_date = fields.Datetime()
    summary_and_decisions = fields.Char()
    eng = fields.Char()
    last_update = fields.Char()

    def create_event(self):
        CalendarEvent = self.env['calendar.event']
        # In Order to test calendar, I will first create One Simple Event with real data
        CalendarEvent.create({
            'start': self.project_start_date,
            'stop': self.project_end_date,
            'name': self.project_name
        })


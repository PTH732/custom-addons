from odoo import models, fields

class People(models.Model):
    _name = 'people2'
    _description = 'People2'

    name = fields.Char(string='Name')

    # Date field
    date = fields.Date(string='Date')

    # Date time field
    datetime = fields.Datetime(string='Date time')

    def action_check(self):
        pass
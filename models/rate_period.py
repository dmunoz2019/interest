from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class InterestRatePeriod(models.Model):
    _name = 'interest.rate.period'
    _description = 'Interest Rate Period'

    name = fields.Char(string='Period Name')
    days_in_period = fields.Integer(string='Days in Period')

    @api.constrains('days_in_period')
    def _check_days_in_period(self):
        for record in self:
            if record.days_in_period <= 0:
                raise ValidationError("Days in period must be greater than zero.")

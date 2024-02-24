# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class InterestRule(models.Model):
    _name = 'interest.rule'
    _description = 'Interest Rule'

    name = fields.Char(string='Name')
    interest_rate = fields.Float(string='Interest Rate (%)')
    condition = fields.Char(string='Condition', help="Python expression to evaluate the rule")
    rate_period_id = fields.Many2one('interest.rate.period', string='Rate Period')

    @api.constrains('interest_rate')
    def _check_interest_rate(self):
        for record in self:
            if record.interest_rate < 0:
                raise ValidationError("Interest rate must not be negative.")

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class InterestRatePeriod(models.Model):
    _name = 'interest.rate.period'
    _description = 'Interest Rate Period'

    name = fields.Char(string='Nombre del periodo', required=True)
    period_type = fields.Selection([
        ('days', 'Días'),
        ('weeks', 'Semanas'),
        ('months', 'Meses'),
        ('years', 'Años')
    ], string='Tipo', required=True, default='days')
    period = fields.Integer(string='Periodo', required=True, default=1)
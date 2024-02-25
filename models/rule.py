# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class InterestRule(models.Model):
    _name = 'interest.rule'
    _description = 'Interest Rule'

    name = fields.Char(string='Nombre', required=True)
    interest_rate = fields.Float(string='Tasa', required=True, help="Tasa de interés en porcentaje. Ejemplo: 5.5 para 5.5%")
    condition = fields.Char(string='Regla', help="Expresión de condición para aplicar la regla. Ejemplo: amount_total > 1000.0")
    rate_period_id = fields.Many2one('interest.rate.period', string='Periodo de tasa', required=True, help="Periodo de tasa de interés")

    @api.constrains('interest_rate')
    def _check_interest_rate(self):
        for record in self:
            if record.interest_rate < 0:
                raise ValidationError("La tasa de interés no puede ser negativa.")

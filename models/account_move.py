from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class AccountMove(models.Model):
    _inherit = 'account.move'

    interest_line_ids = fields.One2many('interest.line', 'invoice_id', string='Líneas de Interés', copy=True)
    calculated_interest = fields.Float(string='Interés calculado', readonly=True)
    overdue_days = fields.Integer(string='Días después de vencimiento', store=True)
    total_with_interest = fields.Float(string='Total con interés',  readonly=True)


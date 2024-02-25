from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class InterestLine(models.Model):
    _name = 'interest.line'
    _description = 'Interest Line'
    name = fields.Char(string='Name')
    invoice_id = fields.Many2one('account.move', string='Factura')
    interest_amount = fields.Float(string='Interés a Pagar', required=True)
    interest_rule_id = fields.Many2one('interest.rule', string='Interés')
    date = fields.Date(string='Fecha', default=date.today())
    
    @api.model
    def create(self, vals):
        invoice_id = vals.get('invoice_id')
        if invoice_id:
            invoice = self.env['account.move'].browse(invoice_id)
            vals['interest_amount'] = vals.get('interest_amount', invoice.calculated_interest)
        return super(InterestLine, self).create(vals)
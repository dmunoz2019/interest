from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class InterestLine(models.Model):
    _name = 'interest.line'
    _description = 'Interest Line'
    name = fields.Char(string='Name')
    invoice_id = fields.Many2one('account.move', string='Invoice')
    interest_amount = fields.Float(string='Interest Amount')
    interest_rule_id = fields.Many2one('interest.rule', string='Interest Rule')
    @api.model
    def create(self, vals):
        invoice_id = vals.get('invoice_id')
        if invoice_id:
            invoice = self.env['account.move'].browse(invoice_id)
            # Use the calculated interest from the invoice if no interest amount is specified
            vals['interest_amount'] = vals.get('interest_amount', invoice.calculated_interest)
        return super(InterestLine, self).create(vals)
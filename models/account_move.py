from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from datetime import date

class AccountMove(models.Model):
    _inherit = 'account.move'

    interest_line_ids = fields.One2many('interest.line', 'invoice_id', string='Líneas de Interés', copy=True)
    calculated_interest = fields.Float(string='Interés calculado', readonly=True)
    overdue_days = fields.Integer(string='Días después de vencimiento', store=True)
    total_with_interest = fields.Float(string='Total con interés', compute='_compute_total_with_interest', readonly=True)

    @api.depends('interest_line_ids', 'interest_line_ids.interest_amount')
    def _compute_interest(self, force=False):
        for invoice in self:
            if invoice.state == 'paid':
                continue

            new_overdue_days = (date.today() - invoice.invoice_date_due).days if invoice.invoice_date_due else 0
            if force or new_overdue_days != invoice.overdue_days:
                invoice.overdue_days = new_overdue_days
                ovd_days = invoice.overdue_days
                if ovd_days > 0:
                    interest_total = 0.0
                    for line in invoice.interest_line_ids:
                        daily_interest_rate = line.interest_rule_id.interest_rate / line.interest_rule_id.rate_period_id.days_in_period
                        interest_for_period = (invoice.amount_total * daily_interest_rate / 100) * ovd_days
                        interest_total += interest_for_period
                        line.interest_amount = interest_for_period
                    invoice.calculated_interest = interest_total
                else:
                    invoice.calculated_interest = 0.0

    @api.depends('amount_total', 'calculated_interest')
    def _compute_total_with_interest(self):
        for invoice in self:
            invoice.total_with_interest = invoice.amount_total + invoice.calculated_interest

    @api.model
    def create(self, vals):
        record = super(AccountMove, self).create(vals)
        record._compute_interest(force=True)
        return record

    def write(self, vals):
        res = super(AccountMove, self).write(vals)
        if 'invoice_payment_term_id' in vals or 'invoice_date_due' in vals:
            self._compute_interest(force=True)
        return res

    @api.model
    def _update_due_date(self):
        invoices = self.search([('state', 'not in', ['draft', 'cancel', 'paid'])])
        for invoice in invoices:
            invoice._compute_interest(force=True)

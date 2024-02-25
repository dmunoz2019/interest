from odoo.tests.common import TransactionCase

class TestInterestCalculation(TransactionCase):

    def setUp(self):
        super(TestInterestCalculation, self).setUp()
        # Preparación: Crear registros necesarios para la prueba
        self.partner = self.env['res.partner'].create({
            'name': 'Test Partner',
        })
        self.product = self.env['product.product'].create({
            'name': 'Test Product',
        })
        self.interest_rate_period = self.env['interest.rate.period'].create({
            'name': 'Monthly',
            'days_in_period': 29,
        })
        self.interest_rule = self.env['interest.rule'].create({
            'name': 'Test Rule',
            'interest_rate': 5.0,
            'rate_period_id': self.interest_rate_period.id,
        })
        # Crear factura (account.move) y relacionarla con una línea de interés
        self.invoice = self.env['account.move'].create({
            'partner_id': self.partner.id,
            'move_type': 'in_invoice',
            'invoice_date': '2024-01-01',
            'invoice_payment_term_id': 4,
            'invoice_line_ids': [(0, 0, {
                'product_id': self.product.id,
                'quantity': 1,
                'price_unit': 1000.0,
            })],
            # Añade más campos requeridos para tu factura aquí
        })
        self.interest_line = self.env['interest.line'].create({
            'invoice_id': self.invoice.id,
            'interest_rule_id': self.interest_rule.id,
            # Añade más campos si es necesario
        })

        self.invoice.action_post()  # Publicar la factura para que se dispare el cálculo de intereses

    def test_interest_calculation(self):
        # Ejecutar el cálculo de intereses
        self.invoice._compute_interest()
        # Verificar que el cálculo de intereses es correcto
        expected_interest = 100.0  # Este es un valor esperado ficticio
        self.assertAlmostEqual(self.interest_line.interest_amount, expected_interest, places=2, msg="El cálculo de intereses no es correcto.")
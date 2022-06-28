# © <2019> <Omar Torres (otorres@proogeeks.com)>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import fields, models


class AccountInvoiceInh(models.Model):
    _inherit = 'account.move'

    ax_exchange_rate = fields.Float(string='Tipo de cambio (MXN/USD)', digits=(12, 4))

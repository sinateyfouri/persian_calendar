from odoo import models, fields, api
import jdatetime
from datetime import datetime
import logging

_logger = logging.getLogger(__name__)

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_order_shamsi = fields.Char(string='Date Order (Shamsi)', compute='_compute_date_order_shamsi', store=False)
    validity_date_shamsi = fields.Char(string='Validity Date (Shamsi)', compute='_compute_validity_date_shamsi', store=False)

    @api.depends('date_order')
    def _compute_date_order_shamsi(self):
        for order in self:
            if order.date_order and self.env.user.lang == 'fa_IR':
                try:
                    # اطمینان از اینکه date_order یه شیء datetimeه
                    gregorian_date = fields.Datetime.to_datetime(order.date_order)
                    _logger.debug(f"Converting date_order {gregorian_date} for order {order.name}")
                    shamsi_date = jdatetime.date.fromgregorian(date=gregorian_date)
                    order.date_order_shamsi = shamsi_date.strftime('%Y/%m/%d')
                    _logger.debug(f"Computed shamsi date: {order.date_order_shamsi}")
                except Exception as e:
                    _logger.error(f"Error converting date_order for order {order.name}: {str(e)}")
                    order.date_order_shamsi = False
            else:
                order.date_order_shamsi = order.date_order

    @api.depends('validity_date')
    def _compute_validity_date_shamsi(self):
        for order in self:
            if order.validity_date and self.env.user.lang == 'fa_IR':
                try:
                    gregorian_date = order.validity_date
                    shamsi_date = jdatetime.date.fromgregorian(date=gregorian_date)
                    order.validity_date_shamsi = shamsi_date.strftime('%Y/%m/%d')
                except Exception as e:
                    _logger.error(f"Error converting validity_date for order {order.name}: {str(e)}")
                    order.validity_date_shamsi = False
            else:
                order.validity_date_shamsi = order.validity_date

class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_date_shamsi = fields.Char(string='Invoice Date (Shamsi)', compute='_compute_invoice_date_shamsi', store=False)
    invoice_date_due_shamsi = fields.Char(string='Due Date (Shamsi)', compute='_compute_invoice_date_due_shamsi', store=False)

    @api.depends('invoice_date')
    def _compute_invoice_date_shamsi(self):
        for move in self:
            if move.invoice_date and self.env.user.lang == 'fa_IR':
                gregorian_date = move.invoice_date
                shamsi_date = jdatetime.date.fromgregorian(date=gregorian_date)
                move.invoice_date_shamsi = shamsi_date.strftime('%Y/%m/%d')
            else:
                move.invoice_date_shamsi = move.invoice_date

    @api.depends('invoice_date_due')
    def _compute_invoice_date_due_shamsi(self):
        for move in self:
            if move.invoice_date_due and self.env.user.lang == 'fa_IR':
                gregorian_date = move.invoice_date_due
                shamsi_date = jdatetime.date.fromgregorian(date=gregorian_date)
                move.invoice_date_due_shamsi = shamsi_date.strftime('%Y/%m/%d')
            else:
                move.invoice_date_due_shamsi = move.invoice_date_due
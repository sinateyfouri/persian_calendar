from odoo import models, fields, api
import jdatetime
from datetime import datetime

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    date_order_shamsi = fields.Char(string='Date Order (Shamsi)', compute='_compute_date_order_shamsi', store=False)
    validity_date_shamsi = fields.Char(string='Validity Date (Shamsi)', compute='_compute_validity_date_shamsi', store=False)


    @api.depends('date_order')
    def _compute_date_order_shamsi(self):
        for order in self:
            if order.date_order and self.env.user.lang == 'fa_IR':
                gregorian_date = fields.Datetime.from_string(order.date_order)
                shamsi_date = jdatetime.date.fromgregorian(date=gregorian_date)
                order.date_order_shamsi = shamsi_date.strftime('%Y/%m/%d')
            else:
                order.date_order_shamsi = order.date_order

    @api.depends('validity_date')
    def _compute_validity_date_shamsi(self):
        for order in self:
            if order.validity_date and self.env.user.lang == 'fa_IR':
                gregorian_date = order.validity_date
                shamsi_date = jdatetime.date.fromgregorian(date=gregorian_date)
                order.validity_date_shamsi = shamsi_date.strftime('%Y/%m/%d')
            else:
                order.validity_date_shamsi = order.validity_date

class AccountMove(models.Model):
    _inherit = 'account.move'

    invoice_date_shamsi = fields.Char(string='Invoice Date (Shamsi)', compute='_compute_invoice_date_shamsi', store=False)
    invoice_date_due_shamsi = fields.Char(string='Due Date (Shamsi)', compute='_compute_invoice_date_due_shamsi', store=False)
    delivery_date_shamsi = fields.Char(string="Delivery Date (Shamsi)", compute='_compute_delivery_date_shamsi', store=False)


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

    
    @api.depends('delivery_date')
    def _compute_delivery_date_shamsi(self):
        for move in self:
            if move.delivery_date and self.env.user.lang == 'fa_IR':
                gregorian_date = move.delivery_date
                shamsi_date = jdatetime.date.fromgregorian(date=gregorian_date)
                move.delivery_date_shamsi = shamsi_date.strftime('%Y/%m/%d')
            else:
                move.delivery_date_shamsi = move.delivery_date

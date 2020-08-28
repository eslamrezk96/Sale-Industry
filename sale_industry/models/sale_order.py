# -*- coding: utf-8 -*-

from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order.line'

    dimension = fields.Integer(string="Dimension", required=False, store=True, )
    size = fields.Integer(string="Size", required=False, )
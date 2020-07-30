# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    sale_order_line_id = fields.Many2one(comodel_name="sale.order.line")
    dimension = fields.Integer(string="Dimension", required=False, related='sale_order_line_id.dimension')
    size = fields.Integer(string="Size", required=False, related='sale_order_line_id.size')
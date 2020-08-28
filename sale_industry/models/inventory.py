# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockMove(models.Model):
    _inherit = 'stock.move'

    dimension_id = fields.Many2one(comodel_name="sale.order.line",)
    dimension = fields.Integer(string="Dimension",store=True, related='dimension_id.dimension')
    size = fields.Integer(string="Size",)

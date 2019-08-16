# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class res_users(models.Model):
    _inherit = "res.users"

    wise_orders = fields.Boolean('Wise pos orders')
    wise_config = fields.Boolean('Wise pos config')
    config_id = fields.Many2one('pos.config', 'POS config')

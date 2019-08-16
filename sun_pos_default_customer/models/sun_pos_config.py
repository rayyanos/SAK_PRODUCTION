from odoo import models, api, fields,tools,  _

class PosConfig(models.Model):
    _inherit = 'pos.config'

    pos_default_cust = fields.Many2one('res.partner', string="POS Default Customer", domain=[('customer','=',True)])

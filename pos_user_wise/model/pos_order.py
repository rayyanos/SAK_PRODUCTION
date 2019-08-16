# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class pos_order(models.Model):
    _inherit = "pos.order"

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self.env.user.wise_config:
            if not args:
                args = [('user_id', '=', self.env.user.id)]
            else:
                args.append(('id', '=', self.env.user.id))
        return super(pos_order, self).search(args, offset=offset, limit=limit, order=order, count=count)

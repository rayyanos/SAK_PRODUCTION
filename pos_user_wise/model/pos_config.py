# -*- coding: utf-8 -*-
from odoo import api, fields, models, _

class pos_config(models.Model):
    _inherit = "pos.config"

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if self.env.user.wise_config:
            if not args:
                args = [('id', '=', self.env.user.config_id.id)]
            else:
                args.append(('id', '=', self.env.user.config_id.id))
        return super(pos_config, self).search(args, offset=offset, limit=limit, order=order, count=count)

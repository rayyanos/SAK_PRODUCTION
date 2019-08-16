odoo.define('sun_pos_default_customer.sun_pos_default_customer', function (require) 
{
"use strict";
// Define Variable
var models = require('point_of_sale.models');
var screens = require('point_of_sale.screens');

    var _super_order = models.Order.prototype;
    models.Order = models.Order.extend({
        initialize: function(attributes,options){
            var result = _super_order.initialize.apply(this,arguments);
            var client = this.get('client')
            if(client == null){
                var client_obj = this.pos.db.get_partner_by_id(this.pos.config.pos_default_cust[0]);
                this.set('client',client_obj);
            }
            return result;
        },
    });
});
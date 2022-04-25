from os import O_CREAT
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    def create_mo(self):
        for record in self:
            bom = record.order_line.product_id.bom_ids.bom_id
            if bom:
                self.env['mrp.production'].create({
                    'product_id': record.order_line.product_id.id,
                    'product_qty': record.order_line.product_uom_qty,
                    'product_uom_id': record.order_line.product_uom_id,
                    'bom_id': record.order_line.product_id.bom_ids.id,
                })
            else:
                pass
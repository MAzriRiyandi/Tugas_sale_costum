from os import O_CREAT
from odoo import _, api, fields, models
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def create_mo(self):
        for record in self:
            for i in record.order_line:
                bom = i.product_id.bom_ids
                if bom:
                    for l in bom:
                        self.env['mrp.production'].create({
                            'product_id': i.product_id.id,
                            'product_qty': i.product_uom_qty,
                            'product_uom_id': i.product_uom.id,
                            'bom_id': l.id,
                            })
                else:
                    pass
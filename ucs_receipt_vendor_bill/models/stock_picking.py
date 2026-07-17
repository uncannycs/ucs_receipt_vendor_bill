from odoo import models, fields, api
from odoo.exceptions import UserError

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    vendor_bill_ids = fields.Many2many(
        'account.move',
        relation='account_move_stock_picking_rel',
        column1='picking_id',
        column2='move_id',
        string='Vendor Bills',
    )

    def action_create_vendor_bill(self):
        self.ensure_one()
        if not self.purchase_id:
            raise UserError("This receipt is not linked to a Purchase Order.")
        
        # Get existing bills on the PO
        existing_bills = self.purchase_id.invoice_ids
        
        # Call action_create_invoice on PO
        action = self.purchase_id.with_context(active_picking_id=self.id).action_create_invoice()
        
        # Find newly created or updated bills
        new_bills = self.purchase_id.invoice_ids - existing_bills
        
        # Link them to this receipt
        if new_bills:
            self.write({'vendor_bill_ids': [(4, bill.id) for bill in new_bills]})
            
        return action

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def action_create_invoice(self):
        # Get existing bills
        existing_bills = self.invoice_ids
        
        # Call super to create new bills
        action = super().action_create_invoice()
        
        # Find new bills
        new_bills = self.invoice_ids - existing_bills
        
        if new_bills:
            for order in self:
                # Find all done incoming receipts for this PO, sorted by date_done
                receipts = order.picking_ids.filtered(
                    lambda p: p.picking_type_code == 'incoming' and p.state == 'done'
                ).sorted('date_done')
                
                # For each new bill for this order
                order_new_bills = new_bills.filtered(lambda b: b.invoice_origin == order.name or order.id in b.line_ids.mapped('purchase_line_id.order_id').ids)
                if not order_new_bills:
                    order_new_bills = new_bills # Fallback if we can't filter correctly
                
                for bill in order_new_bills:
                    # Look for receipts that don't have bills linked yet
                    unbilled_receipt = receipts.filtered(lambda p: not p.vendor_bill_ids)
                    if unbilled_receipt:
                        # Link to the oldest unbilled receipt
                        unbilled_receipt[0].vendor_bill_ids = [(4, bill.id)]
                    else:
                        # If all receipts have bills, just link to the latest one
                        if receipts:
                            receipts[-1].vendor_bill_ids = [(4, bill.id)]
                        
        return action
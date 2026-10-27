from odoo import api, models, fields
from odoo.exceptions import ValidationError

class TextileProductionOrder(models.Model):
    _name = 'textile.production'
    _description = 'Textile Production Order'

    name = fields.Char(string='Nomor Produksi', required=True, copy=False, readonly=True, default="New")
    product_id = fields.Many2one('product.product', string='Produk', required=True)
    quantity = fields.Float(string='Jumlah Produksi', required=True)
    production_date = fields.Date(string='Tanggal Produksi', required=True)
    deadline = fields.Date(string='Batas Waktu')
    responsible_id = fields.Many2one('res.users', string='Penanggung Jawab', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('in_progress', 'In Progress'),
        ('quality_check', 'Quality Check'),
        ("completed", 'Completed'),
    ], string='Status', default='draft', required=True, copy=False)

    @api.constrains("quantity")
    def _check_quantity(self):
        for record in self:
            if record.quantity <= 0:
                raise ValidationError(
                    "Jumlah produksi harus lebih besar dari 0."
                )

    @api.constrains("production_date", "deadline")
    def _check_deadline(self):
        for record in self:
            if (
                record.production_date 
                and record.deadline 
                and record.deadline < record.production_date
            ):
                raise ValidationError(
                    "Batas waktu tidak boleh lebih awal "
                    "dari tanggal produksi."
                )
            
    def action_confirm(self):
        for record in self:
            if record.state != 'draft':
                raise ValidationError(
                    "Hanya pesanan produksi dalam status 'Draft' "
                    "yang dapat dikonfirmasi."
                )
            record.state = 'confirmed'

    def action_start_production(self):
        for record in self:
            if record.state != 'confirmed':
                raise ValidationError(
                    "Hanya pesanan produksi dalam status 'Confirmed' "
                    "yang dapat memulai produksi."
                )
            record.state = 'in_progress'

    def action_send_to_quality(self):
        for record in self:
            if record.state != 'in_progress':
                raise ValidationError(
                    "Hanya pesanan produksi dalam status 'In Progress' "
                    "yang dapat dikirim ke Quality Check."
                )
            record.state = 'quality_check'

    def action_approve_quality(self):
        for record in self:
            if record.state != 'quality_check':
                raise ValidationError(
                    "Hanya pesanan produksi dalam status 'Quality Check' "
                    "yang dapat diselesaikan."
                )
            record.state = 'completed'

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if not vals.get("name") or vals.get("name") == "New":
                vals["name"] = (
                    self.env["ir.sequence"].next_by_code(
                        "textile.production"
                    )
                    or "New"
                )
        return super().create(vals_list)

    def write(self, vals):
        planning_fields = {
            "product_id",
            "quantity",
            "production_date",
            "deadline",
            "responsible_id",
        }

        if planning_fields.intersection(vals):
            for record in self:
                if record.state != "draft":
                    raise ValidationError(
                        "Field planning hanya bisa diubah "
                        "ketika Production Order berstatus Draft."
                    )

        return super().write(vals)
from odoo import fields, models


class Act(models.Model):
    _name = "information.system.act"
    _description = "Act model"

    name = fields.Char(required=True)
    date = fields.Date()
    status = fields.Selection(
        string="Product status",
        selection=[
            ("sale", "Sale"),
            ("buy", "Buy"),
            ("moving", "Moving"),
            ("commission", "Commission"),
        ],
        help="Status",
    )
    previous_warehouse = fields.Many2one(
        "information.system.warehouse", string="Warehouse previous"
    )
    next_warehouse = fields.Many2one(
        "information.system.warehouse", string="Warehouse next"
    )
    product_id = fields.Many2one(
        "information.system.product", string="Product"
    )
    expenses_income = fields.Integer(string="Expenses/Income")
    count_products = fields.Integer()
    user_id = fields.Many2one(
        "res.users",
        string="Salesperson",
        index=True,
        default=lambda self: self.env.user,
    )

    def action_accept_act(self):
        for record in self:
            record.name = "Something"
        return True

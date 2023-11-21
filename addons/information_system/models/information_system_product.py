from odoo import fields, models


class Product(models.Model):
    _name = "information.system.product"
    _description = "Products model"

    name = fields.Char(required=True)
    description = fields.Text()

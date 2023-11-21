from odoo import fields, models


class Product(models.Model):
    _name = "information.system.warehouse"
    _description = "Warehouse model"

    name = fields.Char(required=True)

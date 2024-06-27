from odoo import models, fields


class TODOLine(models.Model):
    _name = "todo.line"
    _description = "TODO Line"

    sequence = fields.Integer(string="Sequence")
    page_id = fields.Many2one("todo.page", string="Page")
    description = fields.Char(string="description")

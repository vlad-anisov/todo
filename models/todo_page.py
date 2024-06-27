from odoo import models, fields


class TODOPage(models.Model):
    _name = "todo.page"
    _description = "TODO Page"

    name = fields.Char(string="Name", default="TODO")
    description = fields.Char(string="Description")
    line_ids = fields.One2many("todo.line", "page_id", string="Lines")

    def add_task(self):
        self.ensure_one()
        if self.description:
            self.env["todo.line"].create({
                "page_id": self.id,
                "description": self.description,
            })
            self.description = ""

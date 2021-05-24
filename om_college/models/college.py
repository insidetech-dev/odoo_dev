from odoo import fields, models

class CollegeDetails(models.Model):
    _name = 'college.colleges'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(string = 'college name', required = True)
    college_number = fields.Integer(string = 'college number')
    address = fields.Text(string = 'address')

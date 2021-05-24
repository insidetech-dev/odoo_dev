from odoo import fields,models

class SchoolDetails(models.Model):
    _name = 'school.table.schools'

    name = fields.Char(string = 'school name')
    school_number = fields.Integer(string = 'school number')
    address = fields.Text(string = 'address')
    win_percentage = fields.Float(string = 'win percentage')
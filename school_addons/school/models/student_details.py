from odoo import models, fields

class StudentDetails(models.Model):
    _name = 'school.table.student'

    name = fields.Char(string = 'student name')
    roll_number = fields.Integer(string = 'roll number')
    school_id = fields.Many2one('school.table.schools', string = "school")


class StudentExtends(models.Model):
    _inherit = 'school.table.schools'


    schools = fields.One2many('school.table.student','school_id',string='school list')
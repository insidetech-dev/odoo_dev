from odoo import fields, models

class CollegeStudent(models.Model):
    _name = 'college.students'

    name = fields.Char(string = 'student name', required=True)
    student_number = fields.Integer(string = 'student number')
    address = fields.Text(string = 'address')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other')

    college_id = fields.Many2one('college.colleges', string ='college')

class StudentExtends(models.Model):
    _inherit = 'college.colleges'

    students = fields.One2many('college.students','college_id',string = 'student list')

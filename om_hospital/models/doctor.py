from odoo import api, fields, models

class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _description = "hospital doctor"

    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other')
    patient_id = fields.Many2one('hospital.patient', string="patient")

class DoctorExtends(models.Model):
    _inherit = 'hospital.patient'

    patients = fields.One2many('hospital.doctor', 'patient_id', string='doctor list')

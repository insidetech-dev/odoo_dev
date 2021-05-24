# -*- coding: utf-8 -*-
from odoo import api, fields, models

class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = "hospital patient"

    name = fields.Char(string='name', required=True, tracking=True)
    age = fields.Integer(string='age', tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], required=True, default='other')
    note = fields.Text(string='Description')
    responsible_id = fields.Many2one('res.partner', string='responsible')
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done'),
        ('cancelled', 'Cancelled')
    ], default='draft', string= 'States')


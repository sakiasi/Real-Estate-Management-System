from odoo import fields, models

class EstateSeller(models.Model):
    _name = 'estate_seller'
    _description = 'Estate Seller'

    name = fields.Char(string='Name', required=True)
    dob = fields.Date(string='Date of Birth')
    address = fields.Text(string='Address')
    contact = fields.Char(string='Content')
    email = fields.Char(string='Email')
    
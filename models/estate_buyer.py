from odoo import models,fields

class EstateBuyer(models.Model):
    _name = 'estate_buyer'
    _description = 'Estate Buyer'

    name = fields.Char(string='Name' , required=True)
    dob = fields.Date(string='Date of Birth')
    address = fields.Text(string='Description')
    contact = fields.Char(string='Contact')
    email = fields.Char(string='Email')
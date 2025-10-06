from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = 'estate_property_type'
    _description = 'Estate Property Type'

    name = fields.Char(string='Name', required=True)
    

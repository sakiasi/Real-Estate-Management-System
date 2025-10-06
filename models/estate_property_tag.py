from odoo import fields, models

class EstateTag(models.Model):
    _name = 'estate_tag'
    _description = 'Estate Tag'


    name = fields.Char(string='Tag', required = True)
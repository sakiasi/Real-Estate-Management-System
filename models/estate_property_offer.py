from odoo import models,fields

class EstateOffer(models.Model):
    _name = 'estate_offer'
    _description = 'Estate Offer'

    price = fields.Float(string='Price')
    status = fields.Selection(
        [
            ('accepted','Accepted'),
            ('refused','Refused'),
        ]
    )
    partner_id = fields.Many2one('res.partner', string='Person', required=True)
    property_id = fields.Many2one('estate.model', string='Property', required=True)

    validity = fields.Integer(string='Validity', default=7)
    date_deadline = fields.Date(string='Deadline')

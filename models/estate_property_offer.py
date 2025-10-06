from odoo import models,fields

class EstateOffer(models.Model):
    _name = 'estate_offer'
    _description = 'Estate Offer'
    _rec_name = 'buyer_id'

    price = fields.Float(string='Price')
    status = fields.Selection(
        [
            ('accepted','Accepted'),
            ('refused','Refused'),
        ]
    )
    property_id = fields.Many2one('estate.model', string='Property', required=True)
    
    buyer_id = fields.Many2one('estate_buyer', string='Buyer')

    validity = fields.Integer(string='Validity', default=7)
    
    date_deadline = fields.Date(string='Deadline')
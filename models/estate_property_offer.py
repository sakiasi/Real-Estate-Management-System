from odoo import models, fields, api
from datetime import timedelta

class EstateOffer(models.Model):
    _name = 'estate_offer'
    _description = 'Estate Offer'
    _rec_name = 'buyer_id'

    price = fields.Float(string='Price')
    status = fields.Selection(
        [
            ('accepted', 'Accepted'),
            ('refused', 'Refused'),
        ]
    )
    property_id = fields.Many2one('estate.model', string='Property', required=True)
    buyer_id = fields.Many2one('estate_buyer', string='Buyer')

    validity = fields.Integer(string='Validity (days)', default=7)

    date_deadline = fields.Date(
        string='Deadline',
        compute='_compute_deadline',
        inverse='_inverse_deadline',
        store=True
    )

    @api.depends('create_date', 'validity')
    def _compute_deadline(self):
        for record in self:
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            record.date_deadline = create_date + timedelta(days=record.validity)

    def _inverse_deadline(self):
        for record in self:
            create_date = record.create_date.date() if record.create_date else fields.Date.today()
            if record.date_deadline:
                delta = record.date_deadline - create_date
                record.validity = delta.days

    @api.onchange('validity')
    def _onchange_validity(self):
        """Update deadline immediately in the UI whenever validity changes"""
        if self.validity:
            create_date = self.create_date.date() if self.create_date else fields.Date.today()
            self.date_deadline = create_date + timedelta(days=self.validity)

    @api.onchange('date_deadline')
    def _onchange_deadline(self):
        """Also update validity if user changes the deadline in the form"""
        if self.date_deadline:
            create_date = self.create_date.date() if self.create_date else fields.Date.today()
            self.validity = (self.date_deadline - create_date).days

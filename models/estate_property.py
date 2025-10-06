from odoo import fields, models, api

class EstateModel(models.Model):
    _name = 'estate.model'
    _description = 'Estate Model'

    name = fields.Char(string="Name", required=True)
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price", readonly=True)
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sqm)")
    facades = fields.Integer(string="Facades")
    garage = fields.Boolean(string="Garage")
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sqm)")
    state = fields.Selection(
        [
            ('new','New'),
            ('offer received','Offer Received'),
            ('offer accepted','Offer Accepted'),
            ('Sold','Sold'),
            ('cancelled','Cancelled'),
        ], default='new'
    )

    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ],
        string="Garden Orientation"
    )
    
    active = fields.Boolean(string='Active')

    property_type_id = fields.Many2one(
    'estate_property_type',
    string="Property Type"
)
    
    # living_area + garden_area    
    total_area = fields.Float(compute='_compute_total', string='Total Area')

    @api.depends('living_area','garden_area')    
    def _compute_total(self):
        for records in self:
            records.total_area = records.living_area * records.garden_area

    offer_ids = fields.One2many('estate_offer','property_id', string='Offers')

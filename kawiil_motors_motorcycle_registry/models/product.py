from odoo import models,fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Overwriting 'detailed_type'
    detailed_type = fields.Selection(selection_add=[
        ('motorcycle', 'Motorcycle'),
        ], ondelete={'motorcycle': 'set product'}
    )
    # New fields
    horsepower = fields.Float()
    top_speed = fields.Float()
    torque = fields.Float()
    battery_capacity = fields.Selection([
            ('xs','Extra Small'),
            ('sm','Small'),
            ('m','Medium'),
            ('lg','Large'),
            ('xl','Extra Large'),
        ],
        string = 'Battery Capacity'
    )
    charge_time = fields.Float()
    range = fields.Float()
    curb_weight = fields.Float()
    make = fields.Char()
    model = fields.Char()
    year = fields.Integer()
    launch_date = fields.Date()

    def _detailed_type_mapping(self):
        return {'motorcycle':'product'}
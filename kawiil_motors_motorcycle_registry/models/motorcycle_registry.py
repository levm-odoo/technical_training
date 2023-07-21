from odoo import models,fields

class MotorcycleRegistry(models.Model) : 
    # As convention : module.model
    _name = 'motorcycle.registry'
    _description = 'Allows the entry and storage of essential motorcycle details'
    # Renaming of fields
    _rec_name = 'registry_number'

     # Fields of the model
    registry_number = fields.Char(string="Registry number", required=True, default=lambda self: self.env['ir.sequence'].next_by_code('motorcycle.registry.number'))
    vin = fields.Char(required=True)
    first_name = fields.Char(required=True)
    last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char(required=True)
    certificate_title = fields.Binary()
    register_date = fields.Date()
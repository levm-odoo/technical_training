import re
from odoo import models,fields,api
from odoo.exceptions import ValidationError

class MotorcycleRegistry(models.Model) : 
    # As convention : module.model
    _name = 'motorcycle.registry'
    _description = 'Allows the entry and storage of essential motorcycle details'
    # Renaming of fields
    _rec_name = 'registry_number'

     # Fields of the model
     #  Through the lambda function we can assign an automatic default value for the Registry number.
     #  Recovering the secuencial record in 'data' through the environment, automatically computes the next number in the secuence
    registry_number = fields.Char(
        copy=False,
        required=True,
        readonly=True,
        string="Registry number",
        default=lambda self: self.env['ir.sequence'].next_by_code('motorcycle.registry.number'))
    vin = fields.Char(required=True)
    #first_name = fields.Char(required=True)
    #last_name = fields.Char(required=True)
    picture = fields.Image()
    current_mileage = fields.Float()
    license_plate = fields.Char(required=True)
    certificate_title = fields.Binary()
    register_date = fields.Date()
    ## Relational fields
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Owner',
        ondelete='cascade',
        #   An error appears when assigned directly
        #required=True
    )
    # related fields
    email = fields.Char(related='partner_id.email')
    phone = fields.Char(related='partner_id.phone')
    # computed fields
    brand = fields.Char(compute='_extract_VIN')
    model = fields.Char(compute='_extract_VIN')
    year = fields.Char(compute='_extract_VIN')


    # Used to force the domain in the Record Rule 'only_active_modify'
    #   Allows to modify those records that has this property as True
    active = fields.Boolean(default=True,readonly=True)


    ## --------------
    ##  Constraints
    ## --------------
    ##   Allows to validate the format of a field when saving the registry after creating or modifying
    @api.constrains('vin')
    def _check_vin(self):
        pattern = re.compile(r'^[A-Z]{4}[0-9]{2}[A-Z0-9]{2}[0-9]{6}')

        for register in self:
            if not re.fullmatch(pattern, register.vin):
                raise ValidationError("""
The pattern that VIN must follow is:
    Make(2 capital letters) + Model(2 capital letters) + Year(2 digits) + Battery capacity(2 capital letters or numbers) + Serial number(6 digits)
        i.e: KAIN220M000234, KAUK21XL847327
""")
    @api.constrains('license_plate')
    def _check_license_plate(self):
        pattern = re.compile(r'^[A-Z]{1,4}\d{1,3}(?:[A-Z]{2})?$')

        for register in self:
            if not re.fullmatch(pattern, register.license_plate):
                raise ValidationError("""
The pattern that the License plate number must follow is:
    1 to 4 Capital letters + 1 to 3 Digits + 2 Capital letters(optional)
        i.e: KLV453, KLR345BL
""")
                                      
    ## ---------------------------
    ##  Compute fields functions
    ## ---------------------------
    ##   Allows to assign a value to fields by calculating its value instead of recovering it from the database
    ##   In this case as the VIN field is used is added in the 'depends' api notation
    @api.depends('vin')
    def _extract_VIN(self):
        '''Using groups to match a pattern in the VIN number, the value of each of the 3 fields that compose the VIN are recovered and assigned to the individual field
        '''
        pattern = re.compile(r'(^[A-Z]{2})([A-Z]{2})([0-9]{2})[A-Z0-9]{2}[0-9]{6}')

        for register in self:
            register.brand = ''
            register.model = ''
            register.year = ''

            vin = register.vin
            if matched := re.search(pattern, '' if vin == False else vin):
                register.brand = matched.group(1)
                register.model = matched.group(2)
                register.year = matched.group(3)
{
    'name' : 'Motorcycle Registry',
    'summary' : 'Manage Registration of Motorcycles',
    'description' : """Motorcycle Registry
====================
This Module is used to keep track of the Motorcycle Registration and Ownership of each motorcycled of the brand.""",
    'license' : 'OPL-1',
    'author' : 'levm-odoo',
    'website' : 'https://www.github.com/levm-odoo',
    'category' : 'Customized Apps/Kawiil',
    'depends' : [
        'base',
        # Used in the model inheritance of the product.template
        'stock',
        'website'
    ],
    'data' : [
        # Security
        #   Groups and access rights
        'security/registry_groups.xml',
        'security/ir.model.access.csv',
        #   Record rules
        'security/registry_security.xml',
        # Data
        'data/registry_data.xml',
        # Views
        'views/registry_menuitems.xml',
        'views/registry_views.xml',
        'views/product_template_views_inherits.xml',
        #   Templates
        'views/templates/registry_web_templates.xml',
        'views/templates/products_web_templates.xml',
    ],
    'demo' : [
        'demo/registry_demo.xml'
    ],
    'application' : True,
}